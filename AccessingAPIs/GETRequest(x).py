# Here is another example of GET request. In this example, we assume an API endpoint which takes in the registration number of a vehicle and returns associated data.

import requests
BASE_URL = 'https://vehicleapi.com'
response = requests.get(f"{BASE_URL}/vehicles/CBA4476")
print(response.status_code)
print(response)