- day1: 로봇 이해하기 및 fastapi 와 socketio 를 이용한 통신 구축하기
  + examples1.py: FastAPI 기본
    - 기본 서버 / Routing
    - get 방식 parameter 전송
    - HTML Template 사용
    - mini proj: 간단한 웹 기반 시계 만들기(mywatch.py)
  + examples2.py: FastAPI 이미지 활용
    - FastAPI 의 Response 를 이용한 이미지 전송
    - Raspberrypi 카메라 활용
    - mini proj: 간단한 cctv 만들기(mycctv.py)
  + examples3.py: FastAPI, Socketio 활용
    - Fastapi 와 Socketio 사용 방법
    - fastapi_socketio 를 이용한 텍스트, 이미지 전송
    - mini proj: 간단한 채팅 프로그램 만들기(myhat.py)

- day2: 로봇 센서, 모터, 카메라 활용하기
  + e1_audio.py: 오디오 장치 제어하기
    - 오디오 재생하기
    - 오디오 정지하기
  + e2_oled.py: OLED 장치 제어하기
    - 텍스트 출력하기
    - 이미지 출력하기
    - 각종 도형 그리기
  + e3_device.py: 마이크로 컨트롤러 제어하기
    - Neopixel 제어하기
    - DC Plug 상태 확인하기
    - Button 상태 확인하기
    - Pir/Touch 센서 정보 확인하기
  + mini_proj (1): OLED, DEVICE 결합 (p1_oled_device.py)
    - OLED 에 실시간 로봇 상태 표시하고, Neoxpixel 연동하기
    - 배터리, 인체/터치 감지 상태 출력
    - 터치 인식 시 Neopixel 연동
  + e4_motion.py: 서보모터를 제어하기
    - 개별 모터 제어하기
    - 모션 데이터를 활용하기
  + e5_vision.py: 카메라 제어하기
    - 카메라 촬영하고, 이미지 불러오기
    - 각종 도형 및 텍스트 출력하기
    - opencv를 이용한 얼굴 찾기 / 나이, 성별 분석하기 - opencv dnn 모듈 활용(공개모델)
    - object detection - opencv dnn 모듈 활용(공개모델), QRcode 인식하기 - python
    - Tflite 를 이용한 Human pose / image classification (Teachable Machine)
  + mini proj (2): OLED, MOTION, VISON 결합(p2_vision_oled_motion.py)
    - OLED 에 스트리밍하는 얼굴 트래킹 로봇
    - 얼굴 인식 / 중심점 찾기 
    - 머리부분 모터를 이용한 얼굴 트래킹
    - OLED 로 이미지 출력 하기

- day3: 웹 기반 로봇 컨트롤러 완성하기
  + 로봇 컨트롤러 구상하기
  + vision, device, motion, oled 기능을 웹과 연동하기
  + Thread, Queue 를 이용한 vision, device 주요 루틴 완성하기
  + HTML 완성하기
