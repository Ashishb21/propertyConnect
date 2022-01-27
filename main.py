from core.config import settings
from fastapi import FastAPI
from app.routers import default
#from db.utils import check_db_connected,close_db_connected




def include_router(app):
    app.include_router(default.router)
    #app.include_router(users.router,tags=['Users'],prefix="/users")
    #app.include_router(token.router,tags=['Token'],prefix="/login")


def start_application():
    app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)
    include_router(app)
    return app


app = start_application()


@app.on_event("startup")
async def app_startup():
    #await check_db_connected()
    pass


@app.on_event("shutdown")
async def app_shutdown():
    #await close_db_connected()
    pass