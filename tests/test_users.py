from config.base_test import BaseTest


class TestUsers(BaseTest):
    def test_users_avatar(self):
        self.api_users.expect_user_avatar_contain_id()

    def test_users_email(self):
        self.api_users.expect_ends_email()

    def test_get_user_by_random_id(self):
        self.api_users.get_random_user_by_id()

    def test_user_not_found(self):
        self.api_users.expect_404_status_code_for_user_not_found()
        