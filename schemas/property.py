from pydantic import BaseModel,EmailStr
from typing import Optional
from enum import Enum
from schemas.propertyclient import PropertyClientSchema

class PropertyType(str,Enum):
    PLOT = 'PLOT'
    KOTHI = 'KOTHI'
    SHOP = 'SHOP'
    BOOTH='BOOTH'
    SCF="SCF"
    SCO="SCO"
    FLAT="FLAT"
    OTHERS="OTHERS"

class PropertySchema(BaseModel):

    propclient:PropertyClientSchema=None
    propertyNo :Optional[str] =None
    propertyType:PropertyType=None
    location:Optional[str] =None
    sublocation:Optional[str]=None
    propertySize:Optional[str]=None
    totalSqYard:Optional[str]=None
    ratePerYard:Optional[str]=None
    PropertyRate:Optional[str]=None
    reference :Optional[str] =None
    comments :Optional[str] =None


class ModifyPropertySchema(BaseModel):
    property_id:str
    name:str



