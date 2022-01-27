import os
from dotenv import load_dotenv
from pathlib import Path


env_path=Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings():

      APP_TITLE :str =os.getenv("APP_TITLE")
      APP_VERSION :str =os.getenv("APP_VERSION")
      MONGODB_DATABASE :str=os.getenv("MONGODB_DATABASE")
      MONGODB_USER_COLLECTION :str=os.getenv("MONGODB_USER_COLLECTION")
      MONGODB_HOST :str= os.getenv("MONGODB_HOST")
      MONGODB_PORT :str= os.getenv("MONGODB_PORT")
      MONGODB_URL :str=f"mongodb://{MONGODB_HOST}:{MONGODB_PORT}"
      SECRET_KEY:str=os.getenv("SECRET_KEY")
      ACCESS_TOKEN_EXPIRE_MINUTES =30
      ALGORITHM:str="HS256"

settings=Settings()
