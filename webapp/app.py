import logging; logging.basicConfig(level=logging.DEBUG)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
import orm
from models import User, Post, Comment
def get_all_users():
    asyncio.ensure_future(orm.create_pool(host='bdm247336490.my3w.com', user='bdm247336490', password='sql05247299', db='bdm247336490_db'))
    return asyncio.ensure_future(User.findAll())
    # u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    # yield from u.save()

def index(request):
    body=b'<h1>Awesome</h1>'
    users= get_all_users()
    for user in users:
        logging.info(user)
    return web.Response(body=body)

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()