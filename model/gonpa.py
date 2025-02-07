from pydantic import BaseModel
from typing import List,Optional
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


class TranslationUpdate(BaseModel):
    languageCode: str  # Must match `Language.code` in the schema
    name: str
    description: str
    description_audio: Optional[str]

class GonpaUpdate(BaseModel):
    image: Optional[str]  # Image URL or path
    geo_location: Optional[str]  # Can be a JSON string or lat-long
    sect: Optional[Sect]  # Sect type
    type: Optional[GonpaType]  # Gonpa type
    contactId: Optional[str]  # ID of the contact person (if updating)
    translations: Optional[List[TranslationUpdate]]  # List of translations


class GonpaTranslationCreate(BaseModel):
    languageCode: str
    name: str
    description: str
    description_audio: str