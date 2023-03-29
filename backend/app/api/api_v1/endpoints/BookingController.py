import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter, Path, status
from fastapi.response import Response
from app.core.business.abstracts.BookngService import BookingService

bookingroutes = APIRouter()
bookingService = BookingService()

@bookingroutes.post("/")
def create_booking_for_user():
    pass

@bookingroutes.get("/")
def get_booking_for_user():
    pass

@bookingroutes.delete("/")
def delete_booking_for_user():
    pass

@bookingroutes.put("/")
def update_booking_for_user():
    pass

