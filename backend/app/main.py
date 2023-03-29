import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import FastAPI
from typing import Any, List, Optional, Dict, Generator
from app.api.api_v1.routes import api_router

app = FastAPI()
app.include_router(api_router)
