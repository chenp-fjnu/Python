from weibo2 import APIClient


APP_KEY='1091732297'
APP_SECRET='664427d14d31da348ee177c88fc45ddb'
CALLBACK_URL = 'http://www.buyinone.cn' # callback url
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url=client.get_authorize_url()

code = "54cb5cb1af35e050878078ced38d5734"
r = client.request_access_token(code)
access_token=r.access_token
expires=r.expires
expires_in=r.expires_in
uid=r.uid
print(access_token)
print(expires)
print(expires_in)
print(uid)