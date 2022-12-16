import tensorflow as tf
from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor

class Model(object):
  def __init__(self):
    # initialize tts model. fastspeech2 or tacotron2
    self.tts_model = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-kss-ko")
    # initialize mb_melgan model
    self.mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-kss-ko")
    # inference
    self.processor = AutoProcessor.from_pretrained("tensorspeech/tts-fastspeech2-kss-ko")

  def predict(self, msg):
    input_ids = self.processor.text_to_sequence(msg)

    mel_before, mel_after, duration_outputs, _, _ = self.tts_model.inference(
      input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
      speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
      speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
      f0_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
      energy_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
    )

    # melgan inference
    audio_before = self.mb_melgan.inference(mel_before)[0, :, 0]
    audio_after = self.mb_melgan.inference(mel_after)[0, :, 0]

    # save to file
    #sf.write('./audio_before.wav', audio_before, 22050, "PCM_16")
    #sf.write('./audio_after.wav', audio_after, 22050, "PCM_16")
    self.final_result = audio_after

  def getFinalResult(self):
    return self.final_result
