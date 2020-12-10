- stt 
arecord -D dmic_sv -c2 -r 16000 -f S32_LE -d 5 -t wav -vv -V streo stream2.raw
sox stream2.raw -c 1 stream.flac
python3 test.py

export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

 - tts
https://github.com/googleapis/python-texttospeech > samples > snippets > quickstart.py
* 설치 > future==0.18.2, google-cloud-texttospeech==2.2.0
