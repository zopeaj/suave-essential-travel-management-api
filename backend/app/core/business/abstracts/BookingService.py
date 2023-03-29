import os, sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.crud.repository.bookingRepository import BookRepository
from app.models.Bookings import Bookings
from typing import Any

class BookingService:
    def __init__(self, bookingRepository):
        self.bookingRepository = bookingRepository

