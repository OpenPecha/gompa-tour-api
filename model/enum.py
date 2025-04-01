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
    JONANG= "JONANG"
    OTHER = "OTHER"


class GonpaType(str, Enum):
    MONASTERY = "MONASTERY"
    NUNNERY = "NUNNERY"
    TEMPLE = "TEMPLE"