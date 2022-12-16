import requests,argparse,os

def get_tts(args):
  data = {
    "text":args.string,
    "hash":"",
    "voice":args.voice, # ['main', 'boy', 'girl' ,....]
    "lang":args.lang, # ['ko', 'en']
    "type":"mp3"
  }

  #res = requests.post(self.SAPI_HOST + '/tts', headers=headers, json=data)
  res = requests.get(args.url, params=data)
  if res.status_code != 200:
    print(f'response error: {res}')
    return

  with open(args.filename, 'wb') as f:
    f.write(res.content)
    print("Ok")

  if args.play:
    os.system(f'play {args.filename}')
  return

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--string', help='Text for TTS', required=True)
  parser.add_argument('--voice', help='Voice_mode (main|boy|girl...)', default='main')
  parser.add_argument('--lang', help='Language (ko|en)', choices =['ko', 'en'],  default='ko')
  parser.add_argument('--filename', help='filename', default='tts.mp3')
  parser.add_argument('--url', help='Url', default='https://oe-sapi.circul.us/v1/tts')
  parser.add_argument('--play', help='play', action='store_true')
  args = parser.parse_args()

  get_tts(args)
