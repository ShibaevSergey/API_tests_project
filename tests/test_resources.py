from config.base_test import BaseTest


class TestResources(BaseTest):
    def test_get_resources(self):
        self.api_resurces.get_all_resource()

    def test_get_random_resource(self):
        self.api_resurces.get_random_resource_by_id()

    def test_resource_not_found(self):
        self.api_resurces.expect_404_status_code_for_resource_not_found()
