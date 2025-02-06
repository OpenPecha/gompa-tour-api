from fastapi import APIRouter, HTTPException, Depends
from prisma import Prisma
from typing import Optional, List
from Config.connection import get_db
from model.festival import FestivalCreate,festivalTranslationCreate

router = APIRouter()

@router.post("/")
async def create_festival(festival: FestivalCreate, db: Prisma = Depends(get_db)):
    try:
        translations_data = [
            {
                "language": {"connect": {"code": t.languageCode}},
                "name": t.name,
                "description": t.description,
                "description_audio": t.description_audio
            }
            for t in festival.translations
        ]
        
        created_festival = await db.festival.create(
            data={
                "start_date": festival.start_date,
                "end_date": festival.end_date,
                "image": festival.image,
                "translations": {
                    "create": translations_data
                }
            },
            include={
                "translations": True
            }
        )
        return created_festival
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{festival_id}")
async def get_festival(festival_id: str, db: Prisma = Depends(get_db)):
    festival = await db.festival.find_first(
        where={"id": festival_id},
        include={"translations": True}
    )
    if not festival:
        raise HTTPException(status_code=404, detail="Festival not found")
    return festival

@router.get("/")
async def get_festivals(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    db: Prisma = Depends(get_db)
):
    where = {}
    if start_date:
        where["start_date"] = {"gte": start_date}
    if end_date:
        where["end_date"] = {"lte": end_date}
    
    festivals = await db.festival.find_many(
        where=where,
        include={"translations": True}
    )
    return festivals



@router.post("/{festival_id}/translations")
async def add_festival_translation(
    festival_id: str,
    translation: festivalTranslationCreate,
    db: Prisma = Depends(get_db)
):
    try:
        # Check if the gonpa exists
        existing_festival = await db.festival.find_first(where={"id": festival_id})
        if not existing_festival:
            raise HTTPException(status_code=404, detail="festival not found")
            
        # Check if translation for this language already exists
        existing_translation = await db.festivaltranslation.find_first(
            where={
                "festivalId": festival_id,
                "languageCode": translation.languageCode
            }
        )
        if existing_translation:
            raise HTTPException(
                status_code=400,
                detail=f"Translation for language {translation.languageCode} already exists"
            )

        # Create new translation
        new_translation = await db.festivaltranslation.create(
            data={
                "festival": {"connect": {"id": festival_id}},
                "language": {"connect": {"code": translation.languageCode}},
                "name": translation.name,
                "description": translation.description,
                "description_audio": translation.description_audio
            }
        )
        return new_translation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{festival_id}/translations/{language_code}")
async def delete_festival_translation(

    festival_id: str,
    language_code: str,
    db: Prisma = Depends(get_db)
):
    try:
        # Check if the translation exists
        existing_translation = await db.festivaltranslation.find_first(
            where={
                "festivalId": festival_id,
                "languageCode": language_code
            }
        )
        if not existing_translation:
            raise HTTPException(
                status_code=404,
                detail=f"Translation for language {language_code} not found"
            )

        # Get total translation count
        translation_count = await db.festivaltranslation.count(
            where={"festivalId": festival_id}
        )
        
        # Prevent deletion if it's the last translation
        if translation_count <= 1:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete the last translation. Gonpa must have at least one translation"
            )

        # Delete the translation
        deleted_translation = await db.festivaltranslation.delete(
            where={
                "languageCode":  language_code,
                "festivalId": festival_id

            }
        )
        return {
            "message": f"Translation for language {language_code} deleted successfully",
            "translation": deleted_translation
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/{fest_id}")
async def delete_pilgrim_site(fest_id: str, db: Prisma = Depends(get_db)):
    try:
        existing_gonpa = await db.festival.find_first(where={"id": fest_id})
        if not existing_gonpa:
            raise HTTPException(status_code=404, detail="festival not found")
            
        deleted_site = await db.festival.delete(
            where={"id": fest_id},
            include={
                "translations": True
            }
        )
        return {"message": "festival site deleted successfully", "site": deleted_site}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
