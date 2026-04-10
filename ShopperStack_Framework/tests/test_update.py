from api.profile.update_api import UpdateAPI
from utils.read_data import read_json

update_api = UpdateAPI()

def test_update(auth_data,headers):
    # read the test data from the JSON file
    data = read_json("test_data/profile.json")

    payload = data["update_user"]
    # call the update method with the valid payload
    response = update_api.update(payload,auth_data,headers)
    assert response.status_code == 200