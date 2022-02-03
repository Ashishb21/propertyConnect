from sqlalchemy import Column,Integer, String,Boolean
from sqlalchemy.orm import relationship
from core.database import Base
from sqlalchemy.sql.schema import ForeignKey

class User(Base):

    __tablename__ = "user"
    id = Column(String,primary_key=True,index=True,nullable=False)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean(),default=True)
    is_superuser = Column(Boolean(),default=False)
    phone_no=Column(Integer)
    items = relationship("Property", back_populates="user")

    def __repr__(self):
        return f"<User {self.email}"

class Property(Base):

    __tablename__ = "property"

    id = Column(String, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    user_id = Column(String, ForeignKey("user.id"))

    user = relationship("User", back_populates="items")