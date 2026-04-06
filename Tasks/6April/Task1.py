""" Task1 : Perform API Testing for the ShopperStack Swagger UI and perform the following actions:-
1. Post a request to register a user
2. Post a request to login
3. Get a request to fetch the user  """
import requests

# post request to register a user
def register():
    payload = {
    "city": "Ajmer",
    "country": "India",
    "email": "naman1@gmail.com",
    "firstName": "Naman",
    "gender": "MALE",
    "lastName": "Jain",
    "password": "4321",
    "phone": 9876543211,
    "state": "Rajasthan",
    "zoneId": "ALPHA"
    }
    # making the request
    response = requests.post("https://www.shoppersstack.com/shopping/shoppers", json=payload,verify=False) # verify = False to pass SSl certificate
    #printing the response
    print(response.text)    
    # checking the status code
    assert response.status_code==201, "Status code is not 201, It is: "+str(response.status_code)
    print("User Registered with status code 201")
    return response.json()['data']['userId'] # returning the userId 

userId = register()

# post request to login
def login():
    payload = {
    "email": "naman1@gmail.com",
    "password": "4321",
    "role": "SHOPPER"
    }
    # making the request
    response = requests.post("https://www.shoppersstack.com/shopping/users/login", json=payload,verify=False)
    # printing the response
    print(response.text)
    # checking the status code
    assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
    print("User logged in with status code 200")
    return response.json()['data']['jwtToken'] # returning the jwtToken

Token = login()

#setting up the bearer token for authorization
headers = {
    "Authorization": "Bearer " + Token
}

# get request to fetch user
# making the request
response = requests.get("https://www.shoppersstack.com/shoppers/userId",headers=headers,verify=False) 
#printing the response
print(response.text)
# checking status code
assert response.status_code==200, "Status code is not 200, It is: "+str(response.status_code)
print("User fetched with status code 200")