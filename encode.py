#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import urllib.request
from bs4 import BeautifulSoup
print(sys.getdefaultencoding())
myfile = open("output.html","r",encoding="utf-8")
print(myfile.read())
su=u"中华人民共和国万岁"
print(su)

print(su.encode('utf-8'))
print(su.encode('gb2312'))
print(su.encode('gbk'))
print(su.encode('gb2312').decode('gb2312'))
print(su.encode('gbk').decode('gb2312'))
# response=urllib.request.urlopen('http://baike.baidu.com/view/21087.htm',)
# if response.getcode() != 200:
#     print("!200")
# content=response.read().decode('utf-8').encode('gb2312')
# print(content)
#soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')