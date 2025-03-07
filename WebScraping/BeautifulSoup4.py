# BeautifulSoup4
# To navigate and search the HTML document using python, a library known as BeautifulSoup can be used. You can read about the library and its functions here.

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Beautiful library takes in an HTML web bage, and provide us python methods to navigate and access the individual tags within it.

# Let us try some example uses:

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#The BeautifulSoup object, represents the document as a nested data structure.
#prettify method print it in a way which is easy to read.
print(soup.prettify())

#Here are some ways to navigate the data structure

print(soup.title)
# <title>The Dormouse's story</title>

print(soup.title.name)
# u'title'

print(soup.title.parent.name)
#u u'head'

print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

print(soup.p['class'])
# u 'title'

links = soup.find_all('a')
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>  
for link in links:
    print(link)

print(soup.find(id='links'))
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>  

#Lets try to get siblings of the p tag
children = soup.p.parent.children
for child in children:
    print("Child:", child)

#or you can go sideways
print('Sibling:', soup.p.next_sibling.next_sibling)

# There are many more techniques which you can use to locate any specific content easily.