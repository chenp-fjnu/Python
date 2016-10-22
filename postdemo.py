# url='https://api.weibo.com/oauth2/access_token?client_id=1091732297&client_secret=664427d14d31da348ee177c88fc45ddb&grant_type=authorization_code&code=fa285a6a6c244f1093bec90a4db3678f&redirect_uri=http://www.buyinone.cn'
# postdata={
# 'client_id':'1091732297',
# 'client_secret':'664427d14d31da348ee177c88fc45ddb',
# 'grant_type':'authorization_code',
# 'code':'fa285a6a6c244f1093bec90a4db3678f',
# 'redirect_uri':'http://www.buyinone.cn' 
# }
# client_id:1091732297
# client_secret:664427d14d31da348ee177c88fc45ddb
# grant_type:authorization_code
# code:54cb5cb1af35e050878078ced38d5734
# redirect_uri:http://www.buyinone.cn 
#How to get the authorize code dynamically.
import urllib.request
from urllib.request import Request
import json
# weiboauthurl='https://api.weibo.com/oauth2/authorize?client_id=1091732297&redirect_uri=http://www.buyinone.cn&response_type=code'
# weibogettokenurl='https://api.weibo.com/oauth2/access_token?client_id=1091732297&client_secret=664427d14d31da348ee177c88fc45ddb&grant_type=authorization_code&code=fa285a6a6c244f1093bec90a4db3678f&redirect_uri=http://www.buyinone.cn'
weixintokenurl='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx478a4ee1cf43c4d8&secret=2faef667da9a80555d11e363682d5df9'
# {"access_token":"KyGEeXVhWpz6-6jiVvMDmsukmf42Xk2E2HAD6FZ5STveBATilYsTFN2al6Es2i5gJ5lY2btucfeRDXpamQi_c1nEBBPwTMN3BpYQfLvbjPexvJM8BSjEBft9V89O1tNJFPQbAFAPZA","expires_in":7200}
# ar = urllib.request.urlopen(authurl)
# print(ar)
# url='https://api.weibo.com/2/friendships/friends.json?access_token=2.00JbjGiB88nsLBeb9e23f61eBN2pJC&uid=1567896867'
# req = urllib.request.Request(url,method='post')
# pdata=urllib.parse.urlencode(postdata).encode()
def getresponse(url):
    r=urllib.request.urlopen(url)
    result=r.read().decode()
    result_dict=json.loads(result)
    print(result_dict)
    r.close()
    return result_dict

result_dict=getresponse(weixintokenurl)
token=result_dict['access_token']
print(token)
weixingetipurl='https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s' % token
getresponse(weixingetipurl)


#qq
#1105773334
#UVXzJUhX3l26NKzt


