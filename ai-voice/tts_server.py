import os
from fastapi import FastAPI
import uvicorn
import log
import uuid
import yaml
import base64
import soundfile as sf

app = FastAPI()
_path = "tmp"
logger = log.configure_logger("main", "tts")

@app.on_event("startup")
async def startup_event():
  global tts_obj
  try:
    import tts_project.tts_inference as tts
    tts_obj = tts.Model()
    logger.info(f'! TTS-SERVER START')
  except Exception as ex:
    logger.info(f'! TTS-SERVER Err: {ex}')

@app.post('/tts')
async def tts(msg):
  try:
    request_id = str(uuid.uuid4())
    logger.info(f'{request_id} - Request')
    tts_obj.predict(msg)
    file_name = f'{_path}/{request_id}.wav'

    sf.write(file_name, tts_obj.getFinalResult(), 22050, "PCM_16")
    with open(file_name, 'rb') as f:
      data = base64.b64encode(f.read()).decode()
    os.remove(file_name)
    logger.info(f'{request_id} - ok')
  except Exception as ex:
    logger.info(f'{request_id} - Err: {ex}')
    return {'type':'tts', 'result':'fail', 'data':""}
  return {'type':'tts', 'result':'ok', 'data':data}

def get_config():
  with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

  env = os.environ.get("PY_ENV")
  if env == None or (env in cfg) == False:
    env = "STG"

  c = cfg[env];
  c["ENVIRONMENT"] = env
  return c

if __name__ == "__main__":
  config = get_config()

  os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
  os.environ["CUDA_VISIBLE_DEVICES"]=str(config["TTS_GPU"])

  logger.info(f'! GPU: {config["TTS_GPU"]}, port: {config["TTS_PORT"]}')
  uvicorn.run('tts_server:app', host="0.0.0.0", port=config["TTS_PORT"])
