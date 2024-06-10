import allure
import requests

from services.register.models.register_model import SuccessfulRegistrationModel, UnsuccessfulRegistrationModel
from utils.errors import Errors
from utils.helper import Helper
from config.headers import Headers
from services.register.payloads import Payloads
from services.register.endpoints import Endpoints


class RegisterAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step('Register new user')
    def register_new_user(self):
        response = requests.post(
            url=self.endpoints.REGISTER,
            json=self.payloads.successful_registration,
        )
        assert response.status_code == 200, Errors.STATUS_CODE_IS_NOT_200_ERROR
        model = SuccessfulRegistrationModel(**response.json())
        return model

    @allure.step('Register new user without password')
    def register_new_user_without_password(self):
        response = requests.post(
            url=self.endpoints.REGISTER,
            json=self.payloads.unsuccessful_registration,
        )
        assert response.status_code == 400, Errors.STATUS_CODE_IS_NOT_400_ERROR
        model = UnsuccessfulRegistrationModel(**response.json())
        return model
