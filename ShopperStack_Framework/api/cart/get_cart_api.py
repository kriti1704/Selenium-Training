from core.base_api import BaseAPI
from utils.config import BASE_URL

class GetCartAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)
    
    def get_to_cart(self,shopper_id,headers):
        return self.api.get(f'/shoppers/{shopper_id}/carts',headers=headers)