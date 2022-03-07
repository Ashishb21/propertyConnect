from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from db.services.propertyservices import PropertyService
from schemas.property import PropertySchema,ModifyPropertySchema,PropertySearchSchema
from schemas.propertyclient import PropertyClientSchema
from core.token import get_currentUser
from db.models.usermodels import User,Property

router = APIRouter()

@router.get("/")
def getAllProperty(db: Session = Depends(get_db)):
    return PropertyService.get_all_Property(db=db)

@router.post("/")
def createProperty(property:PropertySchema,db: Session = Depends(get_db),current_user:User=Depends(get_currentUser)):
    return PropertyService.add_property(property=property,db=db,current_user=current_user)

@router.put("/updateProperty")
def updateProperty(property:ModifyPropertySchema, db: Session = Depends(get_db),current_user:User=Depends(get_currentUser)):
    return PropertyService.update_property(modifyproperty=property,db=db,user=current_user)

@router.delete("/{property_id}")
def deleteProperty(property_id: str, db: Session = Depends(get_db),current_user=Depends(get_currentUser)):
    return PropertyService.delete_property(db=db,id=property_id)

@router.get("/getProperty_byUser")
def getPropertyby_currentUser(db:Session=Depends(get_db),current_user:User=Depends(get_currentUser)):
    property=PropertySchema()
    return PropertyService.get_property_by_user(property=property,db=db,user=current_user)

@router.post("/searchProperty")
def searchPropertyby_currentUser(propertysearch:PropertySearchSchema,db:Session=Depends(get_db),current_user:User=Depends(get_currentUser)):

    return PropertyService.search_property_by_user(propertysearch=propertysearch,db=db,user=current_user)