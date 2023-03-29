import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRoute
from app.api.api_v1.endpoints.AirlineReservationController import airlinereservationroutes
from app.api.api_v1.endpoints.BookingController import bookingroutes
from app.api.api_v1.endpoints.FlightController import flightroutes
from app.api.api_v1.endpoints.HotelsController import hotelsroutes
from app.api.api_v1.endpoints.UserController import userroutes

api_route = APIRoute()
api_route.include_router(airlinereservationroutes, prefix="/airlinereservations", tags=["airlinereservation"])
api_route.include_router(bookingroutes, prefix="/booking", tags=["booking"])
api_route.include_router(flightroutes, prefix="/flight", tags=["flight"])
api_route.include_router(hotelsroutes, prefix="/hotel", tags=["hotel"])
api_route.include_router(userroutes, prefix="/user", tags=["user"])

