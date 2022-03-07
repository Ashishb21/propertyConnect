from fastapi import Depends
from sqlalchemy.orm import Session
from db.models.usermodels import Property,User,PropertyClient
from core.database import get_db
from core.token import get_currentUser
from schemas.property import PropertySchema,ModifyPropertySchema,PropertySearchSchema
import uuid
import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class PropertyService:

    def get_all_Property(db:Session):
        return db.query(Property).all()

    def get_property_by_user(property:PropertySchema,db:Session=Depends(get_db),user:User=Depends(get_currentUser)):

        try:

            db_property= db.query(Property.propertyNo,Property.id,Property.propertySize,
                                  Property.ratePerYard,Property.propertyType,Property.propertyRate,
                                  Property.location,Property.sublocation,
                                  Property.totalSqYard,Property.reference,Property.comments,
                                  PropertyClient.clientName,PropertyClient.clientType,PropertyClient.clientEmail,
                                  PropertyClient.clientMobileno,PropertyClient.clientAddress)\
                                .filter(Property.user_id==user.id)\
                                .filter(Property.client_id==PropertyClient.id).all()
            # for item in db_property:
            #
            #     property.propertyNo=item.propertyNo
                # property.propertyType=item.propertyType
                # property.location=item.location
                # property.sublocation=item.sublocation
                # property.propertySize=item.propertySize
                # property.totalSqYard=item.totalSqYard
                # property.ratePerYard=item.ratePerYard
                # property.propertyRate=item.propertyRate
                # property.reference=item.reference
                # property.comments=item.comments

                #response.append(jsonable_encoder(property))
            return db_property
        except Exception as e:
            return JSONResponse(content={"message":str(e)})

    def add_property(property:PropertySchema,db:Session=Depends(get_db),current_user:User=Depends(get_currentUser)):
        try:

            client_id = uuid.uuid4()
            property_id = uuid.uuid4()

            create_client=PropertyClient(clientName=property.propclient.clientName,
                                        clientAddress=property.propclient.clientAddress,
                                        clientMobileno=property.propclient.clientMobileno,
                                        clientType=property.propclient.clientType,
                                        id=str(client_id),
                                        clientEmail=property.propclient.clientEmail)


            create_property = Property( id=str(property_id),
                                        client_id=str(client_id),
                                        user_id=current_user.id,
                                        propertyType=property.propertyType,
                                        propertyNo=property.propertyNo,
                                        location=property.location,
                                        sublocation=property.sublocation,
                                        propertySize=property.propertySize,
                                        propertyRate=property.propertyRate,
                                        ratePerYard=property.ratePerYard,
                                        totalSqYard=property.totalSqYard,
                                        comments=property.comments,
                                        reference=property.reference,
                                        createdDate=datetime.datetime.utcnow(),
                                        modifiedDate=datetime.datetime.utcnow())


            db.add(create_client)
            db.add(create_property)
            print("record")
            db.commit()
            return {"message": "New Property added successfully "}

        except Exception as e:
            return JSONResponse(content={"message":str(e)})

    def delete_property(id:str,db:Session=Depends(get_db)):
        '''
        Only Authorized users can delete the property listing
        '''
        try:

            db_property=db.query(Property).filter(Property.id==id).first()
            db.delete(db_property)
            db.commit()
            return db_property
        except Exception as e:
            return JSONResponse(content={"message":str(e)})

    def update_property( modifyproperty:ModifyPropertySchema ,db:Session=Depends(get_db),user:User=Depends(get_currentUser)):

       try:

           db_property=db.query(Property).filter(Property.id==modifyproperty.property_id).first()
           db_propertyclient=db.query(PropertyClient).filter(db_property.client_id==PropertyClient.id).first()

           db_property.id=modifyproperty.property_id
           db_property.client_id=db_propertyclient.id
           db_property.user_id=user.id
           db_property.propertyType= modifyproperty.propertyType
           db_property.propertyNo=modifyproperty.propertyNo
           db_property.propertySize=modifyproperty.propertySize
           db_property.ratePerYard=modifyproperty.ratePerYard
           db_property.propertyRate=modifyproperty.propertyRate
           db_property.totalSqYard=modifyproperty.totalSqYard
           db_property.location=modifyproperty.location
           db_property.sublocation=modifyproperty.sublocation
           db_property.reference=modifyproperty.reference
           db_property.comments=modifyproperty.comments
           db_property.modifiedDate=datetime.datetime.utcnow()

           db_propertyclient.clientName=modifyproperty.propclient.clientName
           db_propertyclient.clientType=modifyproperty.propclient.clientType
           db_propertyclient.clientEmail=modifyproperty.propclient.clientEmail
           db_propertyclient.clientMobileno=modifyproperty.propclient.clientMobileno
           db_propertyclient.clientAddress=modifyproperty.propclient.clientAddress


           db.commit()
           db_property_modified = db.query(Property.propertyNo, Property.id, Property.propertySize,
                                  Property.ratePerYard, Property.propertyType, Property.propertyRate,
                                  Property.location, Property.sublocation,
                                  Property.totalSqYard, Property.reference, Property.comments,
                                  PropertyClient.clientName, PropertyClient.clientType, PropertyClient.clientEmail,
                                  PropertyClient.clientMobileno, PropertyClient.clientAddress) \
                                  .filter(Property.id == modifyproperty.property_id) \
                                 .filter(PropertyClient.id == db_property.client_id).all()

           return db_property_modified
       except Exception as e:
           return JSONResponse(content={"message":str(e)})
           # return db.query(Property).filter(Property.id==property.property_id).first()

    def search_property_by_user(propertysearch:PropertySearchSchema,db:Session=Depends(get_db),user:User=Depends(get_currentUser)):
        try:

            db_property = db.query(Property).filter(Property.user_id==user.id)\
                .filter(Property.propertyType==propertysearch.propertyType,Property.location.like('%propertysearch.location%')).all()
                # .filter(Property.location==propertysearch.location).all()
                # .filter(Property.propertyRate==propertysearch.propertyRate).all()

            return db_property

        except Exception as e:
            return JSONResponse(content={"message": str(e)})
