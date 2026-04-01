import requests

# fetch get request for store
""" response = requests.get("https://petstore.swagger.io/v2/store/inventory")
# print the response
print(response.text)

# fetching status code
assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
print("status code is 200")

#fetching Not Availble status
dict = response.json()
print(dict['Not Available']) """

# fetch get request for pet
""" response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=SOLD")
# print the response
print(response.text)
# fetching id
print(response.json()[0]['id']) """

# fetch post request for pet
""" payload = {
  "id": 1002,
  "category": {
    "id": 7,
    "name": "cat"
  },
  "name": "Mary",
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
print(response.text)
assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
print("status code is 200") """


# fetch put request for pet
""" payload = {
  "id": 1002,
  "category": {
    "id": 7,
    "name": "cat"
  },
  "name": "Mi-chan",
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
print(response.text)    
assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
print("status code is 200") """

# fetch delete request for pet
""" response = requests.delete("https://petstore.swagger.io/v2/pet/1002")
print(response.text)
assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
print("status code is 200") """


