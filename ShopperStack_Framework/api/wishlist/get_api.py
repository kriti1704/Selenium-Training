from core.base_api import BaseAPI
from utils.config import BASE_URL

class GetWishlistAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def get_wishlist(self,shopper_id,headers):
        return self.api.get(f'/shoppers/{shopper_id}/wishlist',headers=headers)
    
    