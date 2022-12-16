from fastapi import FastAPI, File, UploadFile
import base64
import uvicorn
from pororo import Pororo
import IPython
from pydub import AudioSegment
import logging
import torch

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global tts_pororo, asr_pororo
    print("INIT- START")
    tts_pororo = Pororo(task='tts', lang='multi')
    asr_pororo = Pororo(task='asr', lang='ko')
    print("INIT- END")
    

@app.post('/tts')
async def tts(msg):
    print("TTS-START")
    a = None 
    #msgs = msg.split(".")
    #for msg in msgs:
    #  print(msg)
    #  if msg == "":
    #    break
    wave = tts_pororo(msg, lang='ko')
    audio = IPython.display.Audio(wave, rate=22050)
    with open('test.wav', 'wb') as f:
      f.write(audio.data)
    #  a = AudioSegment.from_wav("test.wav") if a == None else a + AudioSegment.from_wav("test.wav")
    #a.export("test.wav", format="wav")

    # speech로 바꾼 파일 전송
    with open('test.wav', 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    print("TTS-END")
    #torch.cuda.empty_cache()
    return {'type':'tts', 'result':'Ok', 'data':data}


@app.post('/stt')
async def stt(uploadFile: UploadFile = File(...)):
    with open(uploadFile.filename, 'wb') as f:
        f.write(uploadFile.file.read())

    # text로 바꾼 데이터 전송
    data = asr_pororo(uploadFile.filename)['results'][0]['speech']
    return {'type':'stt', 'result':'Ok', 'data':'{} from stt'.format(data)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9999)
