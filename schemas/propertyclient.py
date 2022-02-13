from pydantic import BaseModel, EmailStr
from enum import Enum

class ClientType(str,Enum):
    BUYER="BUYER"
    SELLER="SELLER"
    OTHERS="OTHERS"

class PropertyClientSchema(BaseModel):
    clientName :str
    clientMobileno: int
    clientEmail: EmailStr
    clientType: ClientType= None
    clientAddress: str

