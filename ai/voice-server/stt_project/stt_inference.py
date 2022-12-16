from pororo import Pororo

class Model(object):
  def __init__(self): 
    self.asr_pororo = Pororo(task='asr', lang='ko')

  def predict(self, file_path):
    self.final_result = self.asr_pororo(file_path)['results'][0]['speech']

  def getFinalResult(self):
    return self.final_result
