import os
from fastapi import FastAPI, File, UploadFile
import uvicorn
import log
import uuid
import yaml

app = FastAPI()
_path = "tmp"
logger = log.configure_logger("main", "stt")

@app.on_event("startup")
async def startup_event():
  global stt_obj
  try:
    import stt_project.stt_inference as stt
    stt_obj = stt.Model()
    logger.info(f'! STT-SERVER START')
  except Exception as ex:
    logger.info(f'! STT-SERVER Err: {ex}')

@app.post('/stt')
async def stt(uploadFile: UploadFile = File(...)):
  try:
    request_id = str(uuid.uuid4())
    logger.info(f'{request_id} - Request')
    file_name = f'{_path}/{request_id}.wav'

    with open(file_name, 'wb') as f:
      f.write(uploadFile.file.read())
    stt_obj.predict(file_name)
    os.remove(file_name)
    data = stt_obj.getFinalResult()
    logger.info(f'{request_id} - ok')
  except Exception as ex:
    logger.info(f'{request_id} - Err: {ex}')
    return {'type':'stt', 'result':'fail', 'data':""}
  return {'type':'stt', 'result':'ok', 'data':data}

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
  os.environ["CUDA_VISIBLE_DEVICES"]=str(config["STT_GPU"])
  logger.info(f'! GPU: {config["STT_GPU"]}, port: {config["STT_PORT"]}')
  uvicorn.run("stt_server:app", host="0.0.0.0", port=config["STT_PORT"])
