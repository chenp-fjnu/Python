#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import urllib.request
from urllib.request import Request
from bs4 import BeautifulSoup
# print(sys.getdefaultencoding())
# myfile = open("output.html","r",encoding="utf-8")
# print(myfile.read())
# su=u"中华人民共和国万岁"
# print(su)

# print(su.encode('utf-8'))
# print(su.encode('gb2312'))
# print(su.encode('gbk'))
# print(su.encode('gb2312').decode('gb2312'))
# print(su.encode('gbk').decode('gb2312'))
root_url="http://weibo.com/p/100808203abae913c49270ad2a0b769cc32a87?k=%E9%9A%94%E5%A3%81%E8%83%A1%E5%B0%8F%E5%A7%90%E7%9A%84%E7%B3%9F%E5%BF%83%E5%BE%80%E4%BA%8B&from=501&_from_=huati_topic"
req=Request(root_url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko')
req.add_header('Cookie','SCF=Avk3biXKVjBd8f0lNb0W993Pka7gTreGZ2u-8DY-ZqCEE_X_xet1x5fwMm2FbgU1g4dCzaV6IKYpKt0WHOWv8RE.; ALF=1507441292; un=15021849012; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWnNAch6LT3rFH8OvH5Ep3e5JpX5KMhUgL.Fo2fSoMR1KqRSoM2dJLoIEqLxKnL1KeL1-BLxKqL1KMLBK-LxKqLBo-L1h2LxKqLBKnLBo8Bg5tt; SUHB=0k1DlrEWlVEbQa; SINAGLOBAL=6468597060573.45.1475905394313; ULV=1475905394736:1:1:1:6468597060573.45.1475905394313:; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; SUB=_2A256_PddDeTxGedL7VUZ-SjEzTuIHXVZiG-VrDV8PUNbmtBeLXTQkW-Ia9zSdycMy42XsuMLnfaL2FDJ9Q..; SSOLoginState=1475905293; YF-V5-G0=46bd339a785d24c3e8d7cfb275d14258; YF-Page-G0=e1a5a1aae05361d646241e28c550f987; _s_tentry=-; Apache=6468597060573.45.1475905394313')
req.add_header('Accept-Encoding','gzip, deflate')
req.add_header('Accept-Language','en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3')
req.add_header('Connection','Keep-Alive')
req.add_header('Accept','text/html, application/xhtml+xml, image/jxr, */*')

postdata= urllib.parse.urlencode([
    ('key1','value1'),
    ('key2','value2'),
    ('key3','value3')
    ])
#response=urllib.request.urlopen(req, data=postdata.encode('utf-8'))
response=urllib.request.urlopen(req)

if response.getcode() != 200:
    print("!200")
content=response.read()
print(content)
#soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')