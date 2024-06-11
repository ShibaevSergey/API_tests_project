import random
import allure
import requests
from services.resource.models.resource_model import ResourceModel
from services.resource.models.resources_model import ResourcesModel
from utils.errors import Errors
from utils.helper import Helper
from config.headers import Headers
from services.resource.endpoints import Endpoints
from services.resource.payloads import Payloads


class ResourceAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step('Get all resource')
    def get_all_resource(self):
        response = requests.get(
            url=self.endpoints.RESOURCE,
        )
        self.attach_response(response.json())
        assert response.status_code == 200, Errors.STATUS_CODE_IS_NOT_200_ERROR
        model = ResourcesModel(**response.json())
        return model

    @allure.step('Get resource by id')
    def get_random_resource_by_id(self):
        def get_id_list() -> []:
            id_list = []
            total = self.get_all_resource().total
            response_all_resources = requests.get(
                url=f'{self.endpoints.RESOURCE}?per_page={total}'
            )
            assert response_all_resources.status_code == 200, Errors.STATUS_CODE_IS_NOT_200_ERROR
            model_resources = ResourcesModel(**response_all_resources.json())
            for data in model_resources.data:
                id_list.append(data.id)
            return id_list
        random_id = random.sample(get_id_list(), 1)
        response = requests.get(
            url=f'{self.endpoints.RESOURCE}/{random_id[0]}'
        )
        self.attach_response(response.json())
        assert response.status_code == 200, Errors.STATUS_CODE_IS_NOT_200_ERROR
        model = ResourceModel(**response.json())
        return model

    @allure.step('Check 404 status code for resource not found')
    def expect_404_status_code_for_resource_not_found(self):
        resource_response = requests.get(
            url=f'{self.endpoints.RESOURCE}',
        )
        users_model = ResourcesModel(**resource_response.json())
        total_count_resources = users_model.total
        response = requests.get(
            url=f'{self.endpoints.RESOURCE}/{total_count_resources + 1}'
        )
        self.attach_response(response.json())
        assert response.status_code == 404, Errors.STATUS_CODE_IS_NOT_404_ERROR
