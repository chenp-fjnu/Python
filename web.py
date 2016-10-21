import sys
sys.path.append(os.path.dirname(__file__)+"/oauth/weibo")

from weibo import APIClient
APP_KEY='1091732297'
APP_SECRET='664427d14d31da348ee177c88fc45ddb'
CALLBACK_URL = 'http://www.buyinone.cn' # callback url
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body='<h1>Hello, %s!<h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]