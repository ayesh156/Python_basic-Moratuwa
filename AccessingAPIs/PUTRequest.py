# PUT Request

# POST request can be used to create a new data entry in the API server. PUT request is used to replace an existing record of data with a new record.

import requests
BASE_URL = 'https://vehicleapi.com'
updated_entity = {  "motorvehicles": {      "vehicle": {"type": "car", "registration_no": "CBB1456",      "make": "Toyota",      "model": "Axio"    },    "owner": {      "first_name": "Amal",      "last_name": "Perera", "nic": "900324770V" }  }}
response = requests.put(f"{BASE_URL}/vehicles/CBB1456", json=updated_entity)
print(response.status_code)
print(response.json())