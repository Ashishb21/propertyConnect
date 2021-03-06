from core.config import settings
from fastapi import FastAPI
from app.routers import default,auth ,users,property
from db.utils import check_db_connected,check_db_disconnected
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from core.database import engine,Base
from core.exceptions import NotAuthenticatedException,not_authenticated_exception_handler
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from logging.config import dictConfig
from core.logger_config import log_config
import logging




#log=logging.getLogger("propertyconnect-logger")

def include_router(app):

    app.include_router(auth.router,tags=['Authorization'])
    app.include_router(users.router,tags=['Users'],prefix='/Users')
    app.include_router(property.router,tags=['Property'],prefix='/Property')
    #app.include_router(default.router)
    #app.include_router(usersold.router, tags=['Users'])


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    #manager.not_authenticated_exception = NotAuthenticatedException
    #app.add_exception_handler(NotAuthenticatedException, not_authenticated_exception_handler)

def start_application():

    # logging
    #dictConfig(log_config)
    app = FastAPI(title="settings.APP_TITLE", version="settings.APP_VERSION")
    include_router(app)
    app.add_middleware(CORSMiddleware,
                       allow_origins=["*"],
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"],)

    configure_static(app)
    #create_tables()
    return app

def create_tables():

    log.info("=====Creating Tables =====")
    Base.metadata.create_all(bind=engine)

# app = start_application()
#
#
# @app.on_event("startup")
# async def app_startup():
#     await check_db_connected()
#
#
# @app.on_event("shutdown")
# async def app_shutdown():
#     await check_db_disconnected()



if __name__ == "__main__":
    app = start_application()


    # @app.on_event("startup")
    # async def app_startup():
    #     await check_db_connected()
    #
    #
    # @app.on_event("shutdown")
    # async def app_shutdown():
    #     await check_db_disconnected()
    uvicorn.run(app, host="127.0.0.1", port=8000)
