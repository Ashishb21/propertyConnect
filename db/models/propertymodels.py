from sqlalchemy import Column,String
from sqlalchemy.sql.schema import ForeignKey
from core.database import Base
from sqlalchemy.orm import relationship

class Property(Base):

    __tablename__ = "property"

    id = Column(String, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="items")