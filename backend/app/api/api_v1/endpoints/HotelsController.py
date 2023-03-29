import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi.response import Response
from fastapi import status, APIRouter
from app.core.business.abstracts.HotelsService import HotelsService

hotelsroutes = APIRouter()
hotelsService = HotelsService()

@hotelsroutes.post("/")
def create_hotel_for_user():
    pass

@hotelsroutes.put("/")
def update_hotel_for_user():
    pass

@hotelsroutes.get("/")
def get_hotel_for_user():
    pass

@hotelsroutes.get("/")
def get_available_hotels_for_user():
    pass

@hotelsroutes.delete("/")
def remove_hotel_data():
    pass

