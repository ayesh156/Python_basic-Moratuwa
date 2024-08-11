## Parameterized GET request

# Try to get google search results by submitting a query

import requests

r = requests.get('https://www.google.com/search?q=Python')
print(r.url)
print(r.status_code)
print(r.text)
