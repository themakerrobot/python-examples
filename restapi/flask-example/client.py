import sys
import requests
import datetime
import json
import base64
import argparse

def demo(args):
  url = '{}/{}'.format(args.url, args.type)
  date = str(datetime.datetime.now())

  if args.type == 'ImageHandler':
    files = {'uploadFile':open('./{}'.format(args.snd_file), 'rb')}
    r = requests.post(url, files=files, headers={'time':date}, timeout=5)
    j = json.loads(r.text)

    print('Recv: {}:{}'.format(j['type'], j['result']))
    with open(args.rcv_file, 'wb') as f:
      f.write(base64.b64decode(j['data']))
    print('Save file ok, {}'.format(args.rcv_file))
  
  if args.type == 'TextHandler':
    r = requests.post(url,headers={'time':date}, data={'msg':args.message}, timeout=5)
    j = json.loads(r.text)

    print('Recv: {}:{}'.format(j['type'], j['result']))
    print('Echo data: {}'.format(j['data']))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--type', help='TextHandler or ImageHandler', default='TextHandler')
  parser.add_argument('--url', help='Server URL(http://IPADDRESS:PORT)', default='http://localhost:8888')
  parser.add_argument('--snd_file', help='Only ImageHandler', default='../data/img.jpg')
  parser.add_argument('--rcv_file', help='Only ImageHandler', default='rcv.jpg')
  parser.add_argument('--message', help='Only TextHandler', default='Hello World')
  args = parser.parse_args()

  print("Configure: {}".format(args))
  demo(args)
