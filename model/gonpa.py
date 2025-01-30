from pydantic import BaseModel
from typing import List
from .enum import Sect, GonpaType

class GonpaTranslationBase(BaseModel):
    languageCode: str
    name: str
    description: str
    description_audio: str

class GonpaCreate(BaseModel):
    image: str
    geo_location: str
    sect: Sect
    type: GonpaType
    contactId: str
    translations: List[GonpaTranslationBase]


class GonpaTranslationCreate(BaseModel):
    languageCode: str
    name: str
    description: str
    description_audio: str