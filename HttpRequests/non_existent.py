# Requesting non-existent resource

import requests

r = requests.get('https://httpbin.org/obvious-incorrect')
print(r.url)
print(r.status_code)
print(r.text)