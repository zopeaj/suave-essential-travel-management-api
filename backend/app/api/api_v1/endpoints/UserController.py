import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi.response import Response
from fastapi import status, APIRouter
from app.core.business.abstracts.UserService import UserService

userroutes = APIRouter()
userService = UserService()

@userroutes.post("/")
def create_user():
    pass

@userroutes.put("/")
def update_user():
    pass

@userroutes.get("/")
def get_user():
    pass

@userroutes.delete("/")
def delete_user():
    pass
