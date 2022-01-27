from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates


router=APIRouter()
templates = Jinja2Templates(directory="templates")


# @router.get("/")
# async def read_root():
#     return {'hello':"world"}

@router.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "FriendConnect - Home"})

@router.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "FriendConnect - Login"})

@router.get("/register", response_class=HTMLResponse)
def get_register(request: Request):
    return templates.TemplateResponse("register.html",{"request": request, "title": "FriendConnect - Register"})
