from core.config import settings
from fastapi import FastAPI
from app.routers import default
from db.utils import check_db_connected,check_db_disconnected
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db.session import engine
from db.base import Base

def include_router(app):
    app.include_router(default.router)
    #app.include_router(users.router,tags=['Users'],prefix="/users")
    #app.include_router(token.router,tags=['Token'],prefix="/login")


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app

def create_tables():
    print("=====Creating Tables =====")
    Base.metadata.create_all(bind=engine)


app = start_application()

@app.on_event("startup")
async def app_startup():
    await check_db_connected()

@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()