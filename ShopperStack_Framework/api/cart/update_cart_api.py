from core.base_api import BaseAPI
from utils.config import BASE_URL

class UpdateCartAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)
    
    def update_to_cart(self,shopper_id,item_id,payload,headers):
        return self.api.put(f'/shoppers/{shopper_id}/carts/{item_id}',json=payload,headers=headers)