import tornado.ioloop
import tornado.web
import json
import base64
from datetime import datetime
import argparse

MAX_PROCESS=1 

class TextHandler(tornado.web.RequestHandler):
  def post(self, *args, **kwargs):
    #param = self.request.headers['time']
    message = self.request.arguments['msg'][0].decode()
    message = "{} from TextHandler".format(message)
    return self.write(bytes(json.dumps({"type":"TextHandler", "result":"ok", "data":message}), 'UTF-8'))

class ImageHandler(tornado.web.RequestHandler):
  def upload_file(self, file, f_name):
    with open(f_name, 'wb') as save_file:
      save_file.write(file['body'])

  def post(self, *args, **kwargs):
    ret = "ok"
    #param = self.request.headers['time']
    request_file = self.request.files['uploadFile'][0]
    
    if request_file:
      ret = "ok"
      file_name = request_file.filename
      self.upload_file(request_file, file_name)
      with open(file_name, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    else:
      ret = "fail"
      data = ""

    return self.write(bytes(json.dumps({'type':'ImageHandler', "result":ret, "data":data}), 'UTF-8'))

def configure_app():
  return tornado.web.Application([
    ("/ImageHandler", ImageHandler),
    ("/TextHandler", TextHandler),
  ])

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--port', help='Port Number', default=8888)
  args = parser.parse_args()
  print("Configure: {}".format(args))
  print("Server Start!!")

  app = configure_app()
  server = tornado.httpserver.HTTPServer(app)
  server.bind(args.port)
  server.start(MAX_PROCESS) # forks one process per cpu 0
  tornado.ioloop.IOLoop.current().start()

