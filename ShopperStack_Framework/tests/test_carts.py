from api.cart.add_cart_api import AddCartAPI
from api.cart.delete_cart_api import DeleteCartAPI
from api.cart.get_cart_api import GetCartAPI
from api.cart.update_cart_api import UpdateCartAPI
from utils.read_data import read_json

# adding product to cart
add = AddCartAPI()
item_id = None
def test_add_to_cart(auth_data,headers):
    global item_id
    shopper_id = auth_data['shopper_id']
    data = read_json("test_data/cart.json")
    payload = data['add_cart']
    response = add.add_to_cart(shopper_id,payload,headers)
    item_id = response.json()['data']['itemId']

    assert response.status_code in [201,409]

# fetching the products in the cart
get = GetCartAPI()
def test_get_from_cart(auth_data,headers):
    shopper_id = auth_data['shopper_id']
    response = get.get_to_cart(shopper_id,headers)

    assert response.status_code == 200

# updating the products in the cart
update = UpdateCartAPI()
def test_update_to_cart(auth_data,headers):
    shopper_id = auth_data['shopper_id']
    data = read_json("test_data/cart.json")
    payload = data['update_cart']
    response = update.update_to_cart(shopper_id,item_id,payload,headers)

    assert response.status_code == 200

# deleting the products from the cart
delete = DeleteCartAPI()
def test_delete_from_cart(auth_data,headers):
    shopper_id = auth_data['shopper_id']
    data = read_json("test_data/cart.json")
    product_id = data['add_cart']['productId']
    response = delete.delete_to_cart(shopper_id,product_id,headers)

    assert response.status_code == 200
