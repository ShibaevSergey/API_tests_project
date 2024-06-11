import allure
import requests
from services.login.models.login_models import SuccessfulLoginModel, UnsuccessfulLoginModel
from utils.errors import Errors
from utils.helper import Helper
from config.headers import Headers
from services.login.payloads import Payloads
from services.login.endpoints import Endpoints


class LoginAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step('Login user')
    def login_user(self):
        response = requests.post(
            url=self.endpoints.LOGIN,
            json=self.payloads.successful_login,
        )
        assert response.status_code == 200, Errors.STATUS_CODE_IS_NOT_200_ERROR
        model = SuccessfulLoginModel(**response.json())
        return model

    @allure.step('Login user without password')
    def login_user_without_password(self):
        response = requests.post(
            url=self.endpoints.LOGIN,
            json=self.payloads.unsuccessful_login,
        )
        assert response.status_code == 400, Errors.STATUS_CODE_IS_NOT_400_ERROR
        model = UnsuccessfulLoginModel(**response.json())
        return model