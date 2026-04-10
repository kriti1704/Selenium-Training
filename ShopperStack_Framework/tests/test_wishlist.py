from api.wishlist.add_api import AddProductAPI
from api.wishlist.get_api import GetWishlistAPI
from api.wishlist.delete_api import DeleteWishlistAPI
from utils.read_data import read_json

# adding a product to wishlist
add = AddProductAPI()
def test_add_to_wishlist(auth_data,headers):
    shopper_id = auth_data['shopper_id']
    payload = read_json("test_data/wishlist.json")
    response = add.add_product(shopper_id, headers, payload)

    assert response.status_code in [201,409]

# fetching the products from wishlist
get = GetWishlistAPI()
def test_get_wishlist(auth_data,headers):
    shopper_id = auth_data['shopper_id']
    response = get.get_wishlist(shopper_id,headers)

    assert response.status_code == 200

# deleting the product from wishlist
delete = DeleteWishlistAPI()
def test_delete_product(auth_data,headers):
    shopper_id = auth_data['shopper_id']
    data = read_json("test_data/wishlist.json")
    product_id = data["productId"]
    response = delete.delete_wishlist(shopper_id,product_id,headers)

    assert response.status_code == 204







