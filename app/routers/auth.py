from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from core.token import create_access_token,oauth2_scheme
from core.database import get_db
from db.models.usermodels import User
from core.hashing import Hasher
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    if not Hasher.verify_password(request.password,user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )

    access_token = create_access_token(data={"sub": user.email})

    # response = {
    #     "id": user.id,
    #     "username": user.username,
    #     "email": user.email,
    #     "is_active": user.is_active,
    #     "is_superuser": user.is_superuser,
    #     "jwtToken": access_token,
    # }

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
def logout(token:str =Depends(oauth2_scheme)):

