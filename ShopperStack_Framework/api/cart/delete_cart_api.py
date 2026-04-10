from core.base_api import BaseAPI
from utils.config import BASE_URL

class DeleteCartAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)
    
    def delete_to_cart(self,shopper_id,product_id,headers):
        return self.api.delete(f'/shoppers/{shopper_id}/carts/{product_id}',headers=headers)