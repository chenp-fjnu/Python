url='https://api.weibo.com/oauth2/access_token?client_id=1091732297&client_secret=664427d14d31da348ee177c88fc45ddb&grant_type=authorization_code&code=e5bc939c942416b7817d897f3349cbab&redirect_uri=http://www.buyinone.cn"'
postdata={
'client_id':'1091732297',
'client_secret':'664427d14d31da348ee177c88fc45ddb',
'grant_type':'authorization_code',
'code':'e5bc939c942416b7817d897f3349cbab',
'redirect_uri':'http://www.buyinone.cn' 
}
# client_id:1091732297
# client_secret:664427d14d31da348ee177c88fc45ddb
# grant_type:authorization_code
# code:54cb5cb1af35e050878078ced38d5734
# redirect_uri:http://www.buyinone.cn 
#How to get the authorize code dynamically.
import urllib.request
from urllib.request import Request
authurl='https://api.weibo.com/oauth2/authorize?client_id=1091732297&redirect_uri=http://www.buyinone.cn&response_type=code'
ar = urllib.request.urlopen(authurl)
print(ar)
pdata=urllib.parse.urlencode(postdata).encode()
r = urllib.request.urlopen(url,pdata)
access_token=r.access_token
expires=r.expires
expires_in=r.expires_in
uid=r.uid
print(access_token)
print(expires)
print(expires_in)
print(uid)