from api.profile.login_api import LoginAPI
from utils.read_data import read_json

login_api = LoginAPI()

def test_login_valid():
    # read the test data from the JSON file
    data = read_json("test_data/profile.json")

    payload = data["login_valid_user"]
    # call the login method with the valid payload
    response = login_api.login(payload)
    assert response.status_code == 200

def test_login_invalid():
    data = read_json("test_data/profile.json")

    payload = data["login_invalid_user"]
    # call the login method with the invalid payload
    response = login_api.login(payload)
    assert response.status_code in [400,401,409]