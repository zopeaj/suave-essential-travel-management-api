import os, sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.crud.repository.flightRepository import FlightRepository
from app.models.Flight import Flight
from typing import List, Any

class FlightService:
    def __init__(self, flightRepository):
        self.flightRepository = flightRepository

