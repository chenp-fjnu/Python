
url="http://www.baidu.com"
import urllib.request
response1=urllib.request.urlopen(url)
print(response1.getcode())
content=response1.read()
print(len(content))

html_doc = """
<html><head><title>The Dormouse's story</title></head>
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
soup = BeautifulSoup(html_doc,'lxml')
print(soup.prettify)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id="link3"))
for link in soup.find_all('a'):
    print('%s %s %s' % (link.name, link['href'], link.get_text()))
print(soup.get_text())
import re
print(soup.find('a',href=re.compile(r"ill")))
print(soup.find('p', class_='title'))