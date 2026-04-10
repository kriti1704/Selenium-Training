from core.base_api import BaseAPI
from utils.config import BASE_URL

class DeleteWishlistAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def delete_wishlist(self, shopper_id, product_id, headers):
        return self.api.delete(f'/shoppers/{shopper_id}/wishlist/{product_id}', headers=headers)