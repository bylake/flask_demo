from gevent import monkey

monkey.patch_all()
from flask import Flask
from gevent import pywsgi

app = Flask(__name__)

print ('ok')
@app.route('/')
def index():
    return 'Hello World'


server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
server.serve_forever()