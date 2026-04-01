""" Task 1: create a function to post a request for pet
fetch id
create a function to update and delete the pet using id """
import requests
# post new pet
def post_pet():
    payload = {
    "id": 1003,
    "category": {
        "id": 12,
        "name": "monkey"
    },
    "name": "Punch",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 0,
        "name": "string"
        }
    ],
    "status": "available"
    }

    response = requests.post("https://petstore.swagger.io/v2/pet", json=payload)
    assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
    print("Pet added successfully with status code 200")
    return response.json()['id']

#fetching id
id = post_pet()

# put request to update the pet
def update_pet(id):
    payload = {
    "id": id,
    "category": {
        "id": 12,
        "name": "monkey"
    },
    "name": "Punch",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 0,
        "name": "string"
        }
    ],
    "status": "sold"
    }

    response = requests.put("https://petstore.swagger.io/v2/pet", json=payload)
    assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
    print("Pet updated successfully with status code 200")

# delete the pet
def delete_pet(id):
    response = requests.delete("https://petstore.swagger.io/v2/pet/"+str(id))
    assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
    print("Pet deleted successfully with status code 200")

update_pet(id)
delete_pet(id)
