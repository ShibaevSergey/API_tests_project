from services.users.api_users import UsersAPI
from services.resource.api_resource import ResourceAPI
from services.register.api_register import RegisterAPI


class BaseTest:
    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_resurces = ResourceAPI()
        self.api_register = RegisterAPI()
