from api.profile.register_api import RegisterAPI
from utils.read_data import read_json

# create an instance of the RegisterAPI class to be used in the test cases
register_api = RegisterAPI()

def test_register_valid():
    # read the test data from the JSON file
    data = read_json("test_data/profile.json")

    payload = data["register_valid_user"]
    # call the register method with the valid payload
    response = register_api.register(payload)
    assert response.status_code in [201,409]

def test_register_invalid():
    data = read_json("test_data/profile.json")

    payload = data["register_invalid_user"]
    # call the register method with the invalid payload
    response = register_api.register(payload)
    assert response.status_code == 400

