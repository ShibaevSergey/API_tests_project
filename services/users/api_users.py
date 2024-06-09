import allure
import random
import re
import requests
from utils.helper import Helper
from config.headers import Headers
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints
from services.users.models.users_model import UsersModel
from services.users.models.user_model import UserModel
from utils.errors import Errors


class UsersAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step('Get a list users from a specific page')
    def get_users_from_page(self, page_number: int):
        response = requests.get(
            url=f'{self.endpoints.USERS_ON_PAGE}{page_number}',
        )
        self.attach_response(response.json())
        assert response.status_code == 200, Errors.STATUS_CODE_IS_NOT_200_ERROR
        model = UsersModel(**response.json())
        return model

    @allure.step("Checking that the user's avatar contains the user's id")
    def expect_user_avatar_contain_id(self):
        users = self.get_users_from_page(2)
        for user in users.data:
            assert str(user.id) in user.avatar, Errors.AVATAR_NOT_CONTAINS_ID_ERROR

    @allure.step("Checking that the user's email ends with @reqres.in")
    def expect_ends_email(self):
        def check_email(pattern: re.Pattern[str], email: str):
            if pattern.match(email):
                return True
            else:
                return False

        users = self.get_users_from_page(2)
        email_pattern = re.compile(r'[\W|\w]*@reqres.in')
        for user in users.data:
            assert check_email(email_pattern, user.email) is True, Errors.EMAIL_NOT_ENDS_REQRES_IN_ERROR

    @allure.step('Get user by id')
    def get_random_user_by_id(self):
        users_response = requests.get(
            url=f'{self.endpoints.USERS}',
        )
        users_model = UsersModel(**users_response.json())

        total_count_users = users_model.total
        random_user = random.randint(1, total_count_users)
        response = requests.get(
            url=f'{self.endpoints.USERS}/{random_user}',
        )
        self.attach_response(response.json())
        assert response.status_code == 200, Errors.STATUS_CODE_IS_NOT_200_ERROR
        model = UserModel(**response.json())
        return model

    @allure.step('Check 404 status code for user not found')
    def expect_404_status_code_for_user_not_found(self):
        users_response = requests.get(
            url=f'{self.endpoints.USERS}',
        )
        users_model = UsersModel(**users_response.json())
        total_count_users = users_model.total
        response = requests.get(
            url=f'{self.endpoints.USERS}/{total_count_users + 1}'
        )
        assert response.status_code == 404, Errors.STATUS_CODE_IS_NOT_404_ERROR

