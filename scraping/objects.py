from bs4 import BeautifulSoup

# To keep things simple and also reproducible, consider the following HTML code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

with open('index.html', 'w') as f:
    f.write(html_doc)
soup = BeautifulSoup(html_doc, 'lxml')

#print(soup.prettify())
#print(soup.p) # print first occurrence of element
#print(soup.find_all('b'))
print(soup.b.name) 

tag = soup.find_all('b')[3]
print(tag.attrs)
print(tag.string)