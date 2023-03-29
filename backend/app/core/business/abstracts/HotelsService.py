import os, sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.crud.repository.hotelRepository import HotelRepository
from app.odels.Hotels import Hotels

class HotelsService:
    def __init__(self, hotelRepository):
        self.hotelRepository = hotelRepository
