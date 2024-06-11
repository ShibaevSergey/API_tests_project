from config.base_test import BaseTest


class TestLogin(BaseTest):
    def test_successful_register(self):
        self.api_login.login_user()

    def test_unsuccessful_register(self):
        self.api_login.login_user_without_password()
