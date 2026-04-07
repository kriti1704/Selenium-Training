import requests
import urllib3
# ignoring ssl certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://www.shoppersstack.com/shopping"

# creating a session
session = requests.Session()

payload = {
    "email": "naman1@gmail.com",
    "password": "4321",
    "role": "SHOPPER"
    }
# making the request
login = session.post(base_url+"/users/login", json=payload,verify=False)
# printing the response
print(login.text)
# checking the status code
assert login.status_code==200, "Status code is not 200, It is: "+str(login.status_code)
print("User logged in with status code 200")

id = login.json()['data']['userId']
token = login.json()['data']['jwtToken']

#setting up the bearer token for authorization
headers = {
    "Authorization": "Bearer " + token
}

# get request to fetch user
# making the request
get_user = session.get(base_url+"/shoppers/"+str(id),headers=headers,verify=False) 
#printing the response
print(get_user.text)
# checking status code
assert get_user.status_code==200, "Status code is not 200, It is: "+str(get_user.status_code)
print("User fetched with status code 200")