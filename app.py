from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'LinkBot'


if __name__ == "__main__":
    app.run()
    
from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, World!")

app = web.Application()
app.router.add_get('/', hello)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
