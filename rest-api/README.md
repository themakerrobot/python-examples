# tornado-server-simple
This is simple REST-API server.(Text/Image)
Using Tornado/Flask

 1. ImageHandler: Image send -> receive -> send 
 2. TextHandler: Echo server

# pre-install
pip3 install tornado
pip3 install flask

# Usage
 1. server
 
tornado_api_server.py [-h] [--port PORT]
or
flask_api_server.py [-h] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --port PORT  Port Number

 2. client
 
client.py [-h] [--type TYPE] [--url URL] [--snd_file SND_FILE]
                 [--rcv_file RCV_FILE] [--message MESSAGE]

optional arguments:
  -h, --help           show this help message and exit
  --type TYPE          TextHandler or ImageHandler
  --url URL            Server URL(http://IPADDRESS:PORT)
  --snd_file SND_FILE  Only ImageHandler
  --rcv_file RCV_FILE  Only ImageHandler
  --message MESSAGE    Only TextHandler

