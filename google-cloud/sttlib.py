import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class Stt(object):
  _defaults = {
   "sample_rate":16000,
  }

  def __init__(self, account_file):
    self.__dict__.update(self._defaults)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = account_file
    self.client = speech.SpeechClient()

  def record(self, timeout=5):
    cmd = "arecord -D dmic_sv -c2 -r 16000 -f S32_LE -d {} -t wav -vv -V streo stream.raw;sox stream.raw -c 1 stream.flac;rm stream.raw".format(timeout)
    os.system(cmd)

  def getText(self, filename="stream.flac", lang="ko-KR"'''en-US'''):
    # Loads the audio into memory
    with io.open(filename, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=self.sample_rate,
        language_code=lang)

    # Detects speech in the audio file
    response = self.client.recognize(config, audio)
    results = []
    for result in response.results:
      results.append(result.alternatives[0].transcript)
    return results
