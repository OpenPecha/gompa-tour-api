from pydantic import BaseModel

class LanguageBase(BaseModel):
    code: str
    name: str