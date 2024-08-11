# Exercise : Extract the topic and the link of the Google search results

# As an exercise , let us try to extract only the search results topic and the link from a google search results web page.

# First, you have to open the specific web page in the web browser and use the Inspect tool to study the structure of the page, specially around the item of interest.

# We are using the following link, which will produce the Google search results for the term "Sri+Lanka"

# https://www.google.com/search?q=Sri+Lanka

# After inspecting the web page html source in the browser, we figured-out the titles of search results are in h3 tags, and only the titles use the h3 tags in entire page. Because of this, we can ask the beautiful soup for the h3 tags, if we need all the titles.
# Since the related link must also be quite close to the title, we decide to check the other siblings of the title. You can iteratively check for a id, class, or a numbered order of the specific child to isolated the necessary data.

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Sri+Lanka'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser', page=2)

# Just all the anchors
anchors = soup('a')
for an in anchors:
    print(an.get('href'))

#Just all the headings
headings = soup('h3')
for heading in headings:
    print(heading.find('div').text)
    print(heading.parent.get('href'))
    print('\n')