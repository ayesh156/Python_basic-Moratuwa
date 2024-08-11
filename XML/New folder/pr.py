import requests
import json
laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'
import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}

page = requests.get(url=glomark_coconut, headers=user_agent) 
soup = BeautifulSoup(page.content,'lxml') 
print(soup.prettify())

title = soup.find(id = 'product-promotion-price')

text = title.get_text() # Will get text from html tags
product_title = text.strip() # Removing special characters like \n (newline)
print(product_title )