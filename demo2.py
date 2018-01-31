from gevent import monkey
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import time
monkey.patch_all()
print ('ok')
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "hello world!"
@app.route("/testAsyn")  #如果没有gevent，则testAsyn和testAsyn2会阻塞其他请求
def testAsyn():
  time.sleep(10)
  return "appear"
@app.route("/testAsyn2")

def testAsyn2():
  time.sleep(20)
  return "haha,get it"

if __name__ == "__main__":
  #app.run(debug = True,host="0.0.0.0",port=5000 )
  http_server = WSGIServer(('0.0.0.0',5000),app,handler_class=WebSocketHandler)
  http_server.serve_forever()