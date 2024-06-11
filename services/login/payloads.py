import os
from dotenv import load_dotenv

load_dotenv()


class Payloads:
    successful_login = {
        'email': 'eve.holt@reqres.in',
        'password': os.getenv("PASSWORD"),
    }

    unsuccessful_login = {
        'email': 'eve.holt@reqres.in',
    }