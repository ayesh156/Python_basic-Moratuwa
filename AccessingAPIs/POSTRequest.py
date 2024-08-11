# POST Request

# POST requests are used to create new data entries in the API server. In this example we are sending new data entry about a vehicle with registration number CBB1456 to be stored at the API server.

import requests
BASE_URL = 'https://vehicleapi.com'
vehicle_entity = {  "motorvehicles": {      "vehicle": {"type": "car", "registration_no": "CBB1456",      "make": "Toyota",      "model": "Premio"    },    "owner": {      "first_name": "Amal",      "last_name": "Perera", "nic": "900324770V" }  }}
response = requests.post(f"{BASE_URL}/vehicles", json=vehicle_entity)
print(response.status_code)
print(response.json())

# we assume that our API server works with JSON data, thus the sent information has to be formatted according to JSON format.

# You may notice that in the requests.post function, we have mentioned json as an argument. If we indicate as an argument like this, Python automatically sets the content type of the HTTP request to “application/json”, meaning that we are sending JSON content. This is required for HTTP requests.