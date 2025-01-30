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