from typing import Optional
from pydantic import BaseModel,EmailStr


#properties required during user creation
class RegisterUser(BaseModel):
    username: str
    email : EmailStr
    password : str
    phone_no: int

class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config:  # to convert non dict obj to json
        orm_mode = True