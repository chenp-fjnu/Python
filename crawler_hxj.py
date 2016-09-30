#!/usr/bin/env python3
# -*- coding: utf-8 -*-

url="http://weibo.com/p/100808203abae913c49270ad2a0b769cc32a87"
import urllib.request
response1=urllib.request.urlopen(url)
print(response1.getcode())
html_doc=response1.read().decode('utf_8')
print(len(html_doc))
print(html_doc)

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc,'lxml')
#, href=r'http://huati.weibo.com/k/%E9%9A%94%E5%A3%81%E8%83%A1%E5%B0%8F%E5%A7%90%E7%9A%84%E7%B3%9F%E5%BF%83%E5%BE%80%E4%BA%8B?from=501'):
print(len(soup.find_all('a')))
for link in soup.find_all('a'):
    print('%s %s %s' % (link.name, link['href'], link.get_text()))
