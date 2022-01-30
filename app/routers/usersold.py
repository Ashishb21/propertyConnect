# from fastapi import APIRouter,Request,Form,Depends,status
# from fastapi.responses import HTMLResponse, RedirectResponse
# from db.session import get_db, DBContext
# from sqlalchemy.orm import Session
# from core.hashing import Hasher
# #from db.services.users import create_new_user ,get_user_by_email , get_user_by_username
# from schemas.users import ShowUser
# from starlette.status import HTTP_400_BAD_REQUEST
# from fastapi.templating import Jinja2Templates
# from fastapi_login import LoginManager
# from core.config import settings
# from fastapi.security import OAuth2PasswordRequestForm
# from datetime import timedelta
# from fastapi.encoders import jsonable_encoder
#
# router =APIRouter()
# templates = Jinja2Templates(directory="templates")
#
# manager = LoginManager(settings.SECRET_KEY, token_url="/login", use_cookie=True)
# manager.cookie_name = "auth"
#
# @router.post("/register")
# def register(request: Request,
#              username: str = Form(...),
#              email: str = Form(...),
#              password: str = Form(...),
#              phoneno: int =Form(...),
#              db: Session = Depends(get_db)):
#
#     invalid = False
#     if get_user_by_username(db=db ,username=username):
#         invalid = True
#     if get_user_by_email(db=db ,email=email):
#         invalid = True
#
#     if not invalid:
#         create_new_user(db=db, user=UserCreate(username=username,
#                                                email=email,
#                                                password=password,
#                                                phone_no=phoneno))
#         response = RedirectResponse("/login", status_code=status.HTTP_302_FOUND)
#         return response
#     else:
#         return templates.TemplateResponse("register.html" ,{"request": request, "title": "Register", "invalid": True},
#                                           status_code=HTTP_400_BAD_REQUEST)
#
#
# @manager.user_loader()
# def get_user(username: str, db: Session = None):
#     if db is None:
#         with DBContext() as db:
#             return get_user_by_username(db=db,username=username)
#
#     return get_user_by_username(db=db,username=username)
#
# def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
#     user = get_user_by_username(db=db,username=username)
#     if not user:
#         return None
#     if not Hasher.verify_password(plain_password=password,hashed_password=user.hashed_password):
#         return None
#     return user
#
#
# @router.post("/login",response_model=ShowUser)
# def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), ):
#     user = authenticate_user(username=form_data.username,password=form_data.password,db=db)
#     if not user:
#         return templates.TemplateResponse("login.html", {"request": request,
#         "title": "Login",
#         "invalid": True}, status_code=status.HTTP_401_UNAUTHORIZED)
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = manager.create_access_token(
#         data={"sub": user.username},
#         expires=access_token_expires
#     )
#
#     resp = RedirectResponse("/tasks", status_code=status.HTTP_302_FOUND)
#     manager.set_cookie(resp,access_token)
#     return resp
#
#
# @router.get("/logout", response_class=RedirectResponse)
# def logout():
#     response = RedirectResponse("/")
#     manager.set_cookie(response, None)
#     return response
#
# @router.get("/home")
# def home( user: UserCreate = Depends(manager)):
#     # user = ShowUser(**dict(user))
#     # return templates.TemplateResponse("home.html", {"request": request, "title": "FriendConnect - Home", "user": user})
#     return user
#
#
# @router.get("/tasks")
# def get_tasks(request: Request, db: Session = Depends(get_db), user: ShowUser = Depends(manager)):
#     return jsonable_encoder(user)
#
# # @app.post("/register")
# # def register(request: Request,
# #              username: str = Form(...),
# #              email: str = Form(...),
# #              name: str = Form(...),
# #              password: str = Form(...),
# #              db: Session = Depends(get_db)):
# #     hashed_password = get_hashed_password(password)
# #     invalid = False
# #     if crud.get_user_by_username(db=db, username=username):
# #         invalid = True
# #     if crud.get_user_by_email(db=db, email=email):
# #         invalid = True
# #
# #     if not invalid:
# #         crud.create_user(db=db, user=schemas.UserCreate(username=username, email=email, name=name,
# #                                                         hashed_password=hashed_password))
# #         response = RedirectResponse("/login", status_code=status.HTTP_302_FOUND)
# #         return response
# #     else:
# #         return templates.TemplateResponse("register.html", {"request": request, "title": "Register", "invalid": True},
# #                                           status_code=HTTP_400_BAD_REQUEST)
