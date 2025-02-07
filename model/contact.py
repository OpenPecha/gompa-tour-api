from pydantic import BaseModel
from typing import List, Optional

class ContactTranslationBase(BaseModel):
    languageCode: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str

class ContactBase(BaseModel):
    email: str
    phone_number: str
    translations: List[ContactTranslationBase]

class TranslationUpdate(BaseModel):
    languageCode: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None

class ContactUpdate(BaseModel):
    email: Optional[str] = None
    phone_number: Optional[str] = None
    translations: Optional[List[TranslationUpdate]] = None