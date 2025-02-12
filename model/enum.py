from enum import Enum

class Role(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

class Sect(str, Enum):
    NYINGMA = "NYINGMA"
    KAGYU = "KAGYU"
    SAKYA = "SAKYA"
    GELUG = "GELUG"
    BHON = "BHON"
    REMEY= "REMEY"
    JONANG= "JONANG"
    SHALU = "SHALU"
    BODONG = "BODONG"
    OTHER = "OTHER"

class GonpaType(str, Enum):
    MONASTERY = "MONASTERY"
    NUNNERY = "NUNNERY"
    TEMPLE = "TEMPLE"
    NGAKPA = "NGAKPA"
    OTHER = "OTHER"