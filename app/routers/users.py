from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from db.services.userservices import UserService
from schemas.users import RegisterUser
from core.token import get_currentUser
from db.models.usermodels import User

router = APIRouter()

@router.get("/")
def getAllUser(db: Session = Depends(get_db)):
    return UserService.get_allUsers(db=db)


@router.post("/")
def createUser(user: RegisterUser, db: Session = Depends(get_db)):
    invalid = False
    if UserService.get_user_by_username(db=db, username=user.username):
        invalid = True
    if UserService.get_user_by_email(db=db, email=user.email):
        invalid = True
    if not invalid:
        return UserService.create_user(user, db)
    else:
        return {"error_message":"User or email already exists "}

@router.get("/me")
def getMe(current_user: User = Depends(get_currentUser)):
    return current_user


@router.put("/{userid}")
def updateUser(userid: str, user: RegisterUser, db: Session = Depends(get_db)):
    return UserService.update_user(id=userid, user=user, db=db)


@router.delete("/{userid}")
def deleteUser(userid: str, db: Session = Depends(get_db)):
    return UserService.delete_user_by_id(id=userid, db=db)