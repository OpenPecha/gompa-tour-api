from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

class PilgrimSiteTranslationBase(BaseModel):
    languageCode: str
    name: str
    description: str
    description_audio: str

class PilgrimSiteTranslationCreate(PilgrimSiteTranslationBase):
    pass

class PilgrimSiteTranslation(PilgrimSiteTranslationBase):
    id: str
    pilgrimSiteId: str

    class Config:
        from_attributes = True

class PilgrimSiteBase(BaseModel):
    image: str
    geo_location: str
    contactId: Optional[str]

class PilgrimSiteCreate(PilgrimSiteBase):
    translations: List[PilgrimSiteTranslationBase]


class PilgrimSiteUpdate(PilgrimSiteBase):
    translations: List[PilgrimSiteTranslationBase]

class PilgrimSite(PilgrimSiteBase):
    id: str
    createdAt: datetime
    updatedAt: datetime
    translations: List[PilgrimSiteTranslation]

    class Config:
        from_attributes = True

class PilgrimSiteTranslationCreate(PilgrimSiteTranslationBase):
    languageCode: str
    name: str
    description: str
    description_audio: str