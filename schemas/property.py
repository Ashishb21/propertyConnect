from pydantic import BaseModel


class PropertySchema(BaseModel):
    property_name :str
    #user_id :str

class ModifyPropertySchema(BaseModel):
    property_id:str
    name:str

