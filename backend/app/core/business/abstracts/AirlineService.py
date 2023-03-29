import os, sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.crud.repository.airlineRepository import AirlineRepository
from app.models.AirlineReservation import AirlineReservation

class AirlineService:
    def __init__(self, airlineRepository):
        self.airlineRepository = airlineRepository


