from core.base_api import BaseAPI
from utils.config import BASE_URL

class AddProductAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def add_product(self, shopper_id, headers, payload):
        return self.api.post(f'/shoppers/{shopper_id}/wishlist', json=payload, headers=headers)