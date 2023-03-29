import os
import sys
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.base import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy create_engine

from app.main import app
from app.db.get_db import get_db


SQLALCHEMY_DATABASE_TEST_URL="sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_TEST_URL, connect_args={"check_same_thread":False}, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

