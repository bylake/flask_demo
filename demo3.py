# coding=utf-8
# Python Version: 3.5.1

# Flask
from flask import Flask

# gevent
from gevent import monkey, sleep
from gevent.pywsgi import WSGIServer
monkey.patch_all()
# gevent end

import time

# Cache
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()
# Cache End

app = Flask(__name__)
app.config.update(DEBUG=True)

@app.route('/asyn/', methods=['GET'])
def test_asyn_one():
    print("asyn has a request!")
    cache.clear()
    timeout = 30
    while (not cache.has('a')) and timeout >0:
        sleep(1)
        timeout = timeout - 1
        print('timeout:', timeout)
    print("a", cache.get('a'))
    return 'hello asyn'


@app.route('/test/', methods=['GET'])
def test():
    cache.set('a', '1')
    return 'hello test'


if __name__ == "__main__":
    # app.run()
    http_server = WSGIServer(('', 5001), app)
    http_server.serve_forever()
    test