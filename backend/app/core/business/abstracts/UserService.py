import os, sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.crud.repository.userRepository import UserRepository
from app.models.User import User
from typing import List, Any, Dict

class UserService:
    def __init__(self, userRepository):
        self.userRepository = userRepository
