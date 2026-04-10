from core.base_api import BaseAPI
from utils.config import BASE_URL

class AddCartAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)
    
    def add_to_cart(self,shopper_id,payload,headers):
        return self.api.post(f'/shoppers/{shopper_id}/carts',json=payload,headers=headers)