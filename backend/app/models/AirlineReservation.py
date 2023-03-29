import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.base import Base
from sqlalchemy import String, Integer, Column

class AirlineReservation(Base):
    id = Column(Integer, primary_key=True)
