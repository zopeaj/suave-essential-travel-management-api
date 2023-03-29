import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi.response import Response
from fastapi import status, APIRouter
from app.core.business.abstracts.FlightService import FlightService

flightroutes = APIRouter()
flightService = FlightService()

@flightroutes.post("/")
def create_flight_for_user():
    pass

@flightroutes.put("/")
def update_flight_for_user():
    pass

@flightroutes.delete("/")
def delete_flight_for_user():
    pass

@flightroutes.get("/")
def get_flight_for_user():
    pass


