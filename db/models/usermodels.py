from sqlalchemy import Column, Numeric, String,Boolean,Enum,DateTime,BigInteger
from sqlalchemy.orm import relationship
from core.database import Base
from sqlalchemy.sql.schema import ForeignKey
import datetime
from schemas.property import PropertyType
from schemas.propertyclient import ClientType

class User(Base):

    __tablename__ = "user"
    id = Column(String,primary_key=True,index=True,nullable=False)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean(),default=True)
    is_superuser = Column(Boolean(),default=False)
    phone_no=Column(BigInteger())
    items = relationship("Property", back_populates="user")

    def __repr__(self):
        return f"<User {self.email}"

class Property(Base):

    __tablename__ = "property"

    id = Column(String, primary_key=True, index=True, nullable=False)
    propertyType=Column(String,Enum(PropertyType,name="property_types"))
    propertyNo=Column(String)
    location=Column(String,index=True)
    sublocation=Column(String,index=True)
    propertySize=Column(String)
    totalSqYard=Column(String)
    propertyRate=Column(String)
    ratePerYard=Column(String)
    comments=Column(String)
    reference=Column(String)
    user_id = Column(String, ForeignKey("user.id"))
    client_id =Column(String,ForeignKey("propertyclient.id"))

    createdDate = Column(DateTime, default=datetime.datetime.utcnow)
    modifiedDate = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="items")
    client=relationship("PropertyClient",back_populates="items1")

class PropertyClient(Base):

    __tablename__="propertyclient"

    id =Column(String,primary_key=True,index=True,nullable=False)
    clientType=Column(String,Enum(ClientType,name="client_types"))
    clientName=Column(String)
    clientMobileno = Column(BigInteger())
    clientEmail = Column(String, nullable=False, index=True)
    clientAddress=Column(String)
    items1=relationship("Property",back_populates="client")




