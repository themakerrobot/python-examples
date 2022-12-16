import requests
import datetime
import json
import base64
import argparse
import os

URL = {
  #'stg':'http://192.168.2.254:58821',
  'stg':'https://stg-neapi.circul.us',
  #'ops':'http://192.168.3.254:59821',
  'ops':'https://ops-neapi.circul.us',
}

def record(filename, timeout=5):
    cmd = "arecord -D dmic_sv -c2 -r 16000 -f S32_LE -d {} -t wav -q -vv -V streo test.raw;sox test.raw -c 1 -b 16 {};rm test.raw".format(timeout, filename)
    os.system(cmd)

def play(filename, out='local', volume='-2000', background=True):
    if background:
        cmd = "omxplayer -o {} --vol {} {} &".format(out, volume, filename)
    else:
        cmd = "omxplayer -o {} --vol {} {}".format(out, volume, filename)
    os.system(cmd)

def main(args):
    url = '{}/{}'.format(URL[args.mode], args.type)
    date = str(datetime.datetime.now())

    if args.type == 'tts':
        msg = args.message
        r = requests.post(url, headers={'time':date}, params={'msg':msg}, timeout=10)
        j = json.loads(r.text)
        print('Recv: {}:{}'.format(j['type'], j['result']))
        with open(args.rcv_file, 'wb') as f:
            f.write(base64.b64decode(j['data']))
        play(filename=args.rcv_file)
        print('Save file ok, {}'.format(args.rcv_file))
        

    if args.type == 'stt':
        if args.snd_file == None:
            record('record.wav')
        files = {'uploadFile':open('./{}'.format(args.snd_file), 'rb')}
        r = requests.post(url, files=files, headers={'time':date}, timeout=10)
        j = json.loads(r.text)
        print('Recv: {}:{}'.format(j['type'], j['result']))
        print('Echo data: {}'.format(j['data']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help='(stg|ops)', default='stg')
    parser.add_argument('--type', help='(tts|stt)', default='tts')
    parser.add_argument('--snd_file', help='Only stt', default=None)
    parser.add_argument('--rcv_file', help='Only tts', default='test.wav')
    parser.add_argument('--message', help='Only tts', default='안녕하세요')
    args = parser.parse_args()
    print("Configure: {}".format(args))
    main(args)

