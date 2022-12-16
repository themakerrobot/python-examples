# 실행방법

$ tts_gen [--opt1 "value1" --opt2 "value2" ....]

# opt(옵션)
string: 텍스트 (필수) 
play: 재생 유무
voice: 목소리 종류 (main|boy|girl|....) - (default:main)
lang: 한영 - (ko|en) - (default: ko)
filename: 저장할 파일 경로/이름 - (default: tts.mp)
url: 호스트 주소 - (default: https://oe-sapi.circul.us/v1/tts)

# 실행
$ tts_gen --string "안녕하세요." --play --voice "main" --lang "ko" --filename "test.mp3" --url "https://oe-sapi.circul.us/v1/tts"
$ Ok

# bin
pyinstaller tts_gen.py -F 
