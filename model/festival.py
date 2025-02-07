from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class FestivalTranslationBase(BaseModel):
    languageCode: str
    name: str
    description: str
    description_audio: Optional[str]

class FestivalTranslation(FestivalTranslationBase):
    id: str
    festivalId: str

    class Config:
        from_attributes = True

class FestivalBase(BaseModel):
    start_date: datetime
    end_date: datetime
    image: str

class FestivalCreate(FestivalBase):
    translations: List[FestivalTranslationBase]

class Festival(FestivalBase):
    id: str
    translations: List[FestivalTranslation]
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

class festivalTranslationCreate(FestivalTranslationBase):
    name: str
    languageCode: str
    description: str
    description_audio: Optional[str]


class FestivalTranslationUpdate(BaseModel):
    languageCode: str
    name: Optional[str] = None
    description: Optional[str] = None
    description_audio: Optional[str] = None

class FestivalUpdate(BaseModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    image: Optional[str] = None
    translations: Optional[List[FestivalTranslationUpdate]]  # List of translations

