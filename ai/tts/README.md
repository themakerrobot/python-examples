# 실행방법

$ python3 main.py [--opt1 "value1" --opt2 "value2" ....]

# opt(옵션)
string: 텍스트 (필수) 
voice: 목소리 종류 (main|boy|girl|....) - (default:main)
lang: 한영 - (ko|en) - (default: ko)
filename: 저장할 파일 경로/이름 - (default: tts.mp)
url: 호스트 주소 - (default: https://oe-sapi.circul.us/v1/tts)

# 실행
$ python3 main.py --string "안녕하세요." --voice "main" --lang "ko" --filename "test.mp3" --url "https://oe-sapi.circul.us/v1/tts"
$ Ok
