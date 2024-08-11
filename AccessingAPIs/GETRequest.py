# GET Requests

# Here is an example GET request to retrieve vehicle information from the imaginary API we created, which is having the base URL https://vehicleapi.com. According the API endpoint table shown above, the API endpoint for retrieving vehicle information is BASEURL/vehicles.

# Thus, we create a GET request to BASEURL/vehicles. You can see that there is a variable called response which is assigned the return value of the requests.get() function call. The vehicle records received by the GET requests are captured in this variable. After the GET request is completed, we can process the received data.

import requests
BASE_URL = 'https://vehicleapi.com'
response = requests.get(f"{BASE_URL}/vehicles")
print(response.status_code)
print(response.json())