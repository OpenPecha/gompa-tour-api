from pydantic import BaseModel
from typing import List

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