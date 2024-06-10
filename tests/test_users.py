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

    def test_create_user(self):
        self.api_users.user()

    def test_update_from_put_user(self):
        self.api_users.update_from_put_random_user()

    def test_update_from_patch_user(self):
        self.api_users.update_from_patch_random_user()

    def test_delete_user(self):
        self.api_users.delete_random_user()