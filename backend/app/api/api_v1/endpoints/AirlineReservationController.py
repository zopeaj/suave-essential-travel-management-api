import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter, Path
from app.core.business.abstracts.AirlineService import AirlineService

airlinereservationroutes = APIRouter()
airlineService = AirlineService()

@airlinereservationroutes.post("/")
def create_airline_reservation_for_user():
    pass

@airlinereservationroutes.update("/")
def update_airline_reservation_for_user():
    pass

@airlinereservationroutes.delete("/")
def delete_airline_reservation_for_user():
    pass

@airlinereservationroutes.put("/")
def update_airline_reservation_for_user():
    pass
