from flask import Flask, jsonify, request
import base64
import argparse

app = Flask (__name__)
 
@app.route('/TextHandler', methods = ['POST'])
def text():
  rcv_msg = request.form['msg']
  return jsonify({'type':'TextHandler', "result":"Ok", "data":"{} from TextHandler".format(rcv_msg)})

@app.route('/ImageHandler', methods = ['POST'])
def image():
  rcv_file = request.files['uploadFile']
  rcv_file.save('tmp.jpg')
  with open('tmp.jpg', 'rb') as f:
    data = base64.b64encode(f.read()).decode()
  return jsonify({'type':'ImageHandler', "result":"Ok", "data":data})

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--port', help='Port Number', default=8888)
  args = parser.parse_args()
  print("Configure: {}".format(args))
  print("Server Start!!")
  app.run(port=args.port)
