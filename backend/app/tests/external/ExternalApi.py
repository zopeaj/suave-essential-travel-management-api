from fastapi import client
from app.exceptions import RequestNotFoundException, InvalidaException


class ExternalAPi:
    def __init__(self):
        pass

    def buy_service():
        try:
            request = client.get()
        finally:
            pass
        except (RequestNotFoundException, InvalidaException):
            pass

