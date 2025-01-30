# app/models/statue.py
from pydantic import BaseModel
from typing import List
from datetime import datetime

class StatueTranslationBase(BaseModel):
    languageCode: str
    name: str
    description: str
    description_audio: str

class StatueCreate(BaseModel):
    image: str
    translations: List[StatueTranslationBase]

class StatueResponse(BaseModel):
    id: str
    image: str
    createdAt: datetime
    updatedAt: datetime
    translations: List[StatueTranslationBase]

# app/routes/statue.py
from fastapi import APIRouter, HTTPException, Depends
from prisma import Prisma
from typing import List, Optional
from Config.connection import get_db

from model.statue import StatueCreate, StatueResponse, StatueTranslationBase

router = APIRouter(
)

@router.post("/", response_model=StatueResponse)
async def create_statue(statue: StatueCreate, db: Prisma = Depends(get_db)):
    try:
        translations_data = [
            {
                "language": {"connect": {"code": t.languageCode}},
                "name": t.name,
                "description": t.description,
                "description_audio": t.description_audio
            }
            for t in statue.translations
        ]
        
        created_statue = await db.statue.create(
            data={
                "image": statue.image,
                "translations": {
                    "create": translations_data
                }
            },
            include={
                "translations": True
            }
        )
        return created_statue
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{statue_id}", response_model=StatueResponse)
async def get_statue(statue_id: str, db: Prisma = Depends(get_db)):
    statue = await db.statue.find_unique(
        where={"id": statue_id},
        include={"translations": True}
    )
    if not statue:
        raise HTTPException(status_code=404, detail="Statue not found")
    return statue

@router.get("/", response_model=List[StatueResponse])
async def get_statues(
    language: Optional[str] = None,
    db: Prisma = Depends(get_db)
):
    where = {}
    include = {
        "translations": True
    }
    
    if language:
        include["translations"] = {
            "where": {
                "languageCode": language
            }
        }

    statues = await db.statue.find_many(
        where=where,
        include=include
    )
    return statues

@router.put("/{statue_id}", response_model=StatueResponse)
async def update_statue(
    statue_id: str,
    statue: StatueCreate,
    db: Prisma = Depends(get_db)
):
    try:
        # First, delete existing translations
        await db.statuetranslation.delete_many(
            where={"statueId": statue_id}
        )
        
        # Then update the statue with new data
        updated_statue = await db.statue.update(
            where={"id": statue_id},
            data={
                "image": statue.image,
                "translations": {
                    "create": [
                        {
                            "language": {"connect": {"code": t.languageCode}},
                            "name": t.name,
                            "description": t.description,
                            "description_audio": t.description_audio
                        }
                        for t in statue.translations
                    ]
                }
            },
            include={
                "translations": True
            }
        )
        return updated_statue
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{statue_id}")
async def delete_statue(statue_id: str, db: Prisma = Depends(get_db)):
    try:
        await db.statue.delete(
            where={"id": statue_id}
        )
        return {"message": "Statue deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{statue_id}/translations")
async def add_statue_translation(
    statue_id: str,
    translation: StatueTranslationBase,
    db: Prisma = Depends(get_db)
):
    try:
        # Check if the statue exists
        existing_statue = await db.statue.find_first(where={"id": statue_id})
        if not existing_statue:
            raise HTTPException(status_code=404, detail="Statue not found")
            
        # Check if translation for this language already exists
        existing_translation = await db.statuetranslation.find_first(
            where={
                "statueId": statue_id,
                "languageCode": translation.languageCode
            }
        )
        if existing_translation:
            raise HTTPException(
                status_code=400,
                detail=f"Translation for language {translation.languageCode} already exists"
            )

        # Create new translation
        new_translation = await db.statuetranslation.create(
            data={
                "statue": {"connect": {"id": statue_id}},
                "language": {"connect": {"code": translation.languageCode}},
                "name": translation.name,
                "description": translation.description,
                "description_audio": translation.description_audio
            }
        )
        return new_translation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{statue_id}/translations/{language_code}")
async def delete_statue_translation(
    statue_id: str,
    language_code: str,
    db: Prisma = Depends(get_db)
):
    try:
        # Check if the translation exists
        existing_translation = await db.statuetranslation.find_first(
            where={
                "statueId": statue_id,
                "languageCode": language_code
            }
        )
        if not existing_translation:
            raise HTTPException(status_code=404, detail="Translation not found")

        # Delete translation
        await db.statuetranslation.delete(
            where={"id": existing_translation.id}
        )

        return {"message": "Translation deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
