from config.base_test import BaseTest


class TestRegister(BaseTest):
    def test_successful_register(self):
        self.api_register.register_new_user()

    def test_unsuccessful_register(self):
        self.api_register.register_new_user_without_password()