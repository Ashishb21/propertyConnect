from fastapi import Depends
from sqlalchemy.orm import Session
from db.models.usermodels import User
from core.database import get_db
from schemas.users import RegisterUser
import uuid
from core.hashing import Hasher

class UserService:

    def get_allUsers(db: Session):
        return db.query(User).all()

    def get_user_by_email(email: str ,db:Session=Depends(get_db)):
        return db.query(User).filter(User.email==email).first()

    def get_user_by_username(username:str ,db:Session=Depends(get_db)):
        return db.query(User).filter(User.username==username).first()

    def get_user_by_id(id:str,db:Session=Depends(get_db)):
        db.query(User).filter(User.id==id).first()

    def create_user(registeruser:RegisterUser,db:Session=Depends(get_db)):
       id=uuid.uuid4()
       while UserService.get_user_by_id(id=str(id) ,db=db):
           id =uuid.uuid4()

       db_user= User(id=str(id),
                     email=registeruser.email,
                     username=registeruser.username,
                     hashed_password=Hasher.get_password_hash(registeruser.password),
                     phone_no=registeruser.phone_no)
       db.add(db_user)
       db.commit()
       db.refresh(db_user)
       db_user.hashed_password=None

       return db_user

    def delete_user_by_id(id:str,db:Session=Depends(get_db)):
        db_user=db.query(User).filter(User.id==id).first()
        db.delete(db_user)
        db.commit()
        return db_user

    def update_user(id :str ,user:RegisterUser,db:Session=Depends(get_db)):
        db_user=db.query(User).filter(User.id==id).first()
        db_user.username=user.username
        db_user.email=user.email
        db_user.hashed_password=Hasher.get_password_hash(user.password)
        db_user.phone_no=user.phone_no
        db.commit()
        db_user = db.query(User).filter(User.id == id).first()
        return db_user