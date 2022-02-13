from fastapi import Depends
from sqlalchemy.orm import Session
from db.models.usermodels import Property,User,PropertyClient
from core.database import get_db
from core.token import get_currentUser
from schemas.property import PropertySchema,ModifyPropertySchema
import uuid
import datetime


class PropertyService:

    def get_all_Property(db:Session):
        return db.query(Property).all()

    def get_property_by_user(db:Session=Depends(get_db),user:User=Depends(get_currentUser)):

        return db.query(Property).filter(Property.user_id==user.id).all()

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


            create_property = Property(id=str(property_id),
            client_id=str(client_id),
            user_id=current_user.id,
            propertyType=property.propertyType,
            propertyNo=property.propertyNo,
            location=property.location,
            sublocation=property.sublocation,
            propertySize=property.propertySize,
            propertyRate=property.PropertyRate,
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

        except Exception as e:
            return e

        return {"message":"New Property added successfully "}


    def delete_property(id:str,db:Session=Depends(get_db)):
        '''
        Only Authorized users can delete the property listing
        '''

        db_property=db.query(Property).filter(Property.id==id).first()
        db.delete(db_property)
        db.commit()
        return db_property

    def update_property( property:ModifyPropertySchema ,db:Session=Depends(get_db),user:User=Depends(get_currentUser)):
       db_propery=db.query(Property).filter(Property.id==property.property_id).first()
       db_propery.id=property.property_id
       db_propery.name=property.name
       db_propery.user_id=user.id
       db.commit()
       return db.query(Property).filter(Property.id==property.property_id).first()



