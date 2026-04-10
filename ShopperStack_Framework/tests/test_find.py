from api.profile.find_api import FindAPI

find_api = FindAPI()

def test_find(auth_data, headers):
    response = find_api.find(auth_data, headers)
    assert response.status_code == 200