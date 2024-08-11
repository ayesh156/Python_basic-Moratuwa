# HTTP requests in Python

# We can use the requests module to easily retrieve a web content using HTTP into your python program.

import requests

payload = {'q':'sri+lanka'}
r = requests.get('https://www.google.com/search?', payload)
print(r.url)
print(r.text)