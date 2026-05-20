import requests  # 인터넷을 통해 외부 서버와 데이터를 주고받기 위한 라이브러리를 가져옵니다.
import os        # 라즈베리파이 운영체제(OS)의 시스템 명령어를 실행하기 위한 라이브러리를 가져옵니다.
import time      # 프로그램에 대기 시간(딜레이)을 주거나 시간을 제어하기 위한 라이브러리를 가져옵니다.

API_KEY = "Enter your API key here"  # OpenWeatherMap 사이트에서 발급받은 개인 고유 API 인증 키를 저장합니다.
url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"  # 서울의 현재 날씨 데이터를 섭씨온도(&units=metric)로 요청할 웹 주소를 생성합니다.

def speak(option, msg):  # espeak 프로그램을 사용해 문장을 음성으로 출력하는 함수를 정의합니다.
    os.system("espeak {} '{}'".format(option, msg))  # 라즈베리파이 터미널에 espeak 설정 옵션과 출력할 대사 문자열을 결합하여 실행합니다.

try:  # 프로그램 실행 중 오류가 발생하거나 강제 종료 요청이 올 때를 대비하는 예외 처리 구문을 시작합니다.
    while 1:  # 사용자가 강제로 종료하기 전까지 내부 코드를 무한히 반복하여 실행합니다.
        response = requests.get(url)  # 설정한 웹 주소(url)로 날씨 데이터를 보내달라고 인터넷으로 요청합니다.
        data = response.json()  # 서버로부터 받은 텍스트 응답 데이터를 파이썬이 다루기 쉬운 JSON(딕셔너리) 구조로 변환합니다.
        temp = data["main"]["temp"]  # 전체 변환된 날씨 데이터 중에서 현재 '기온' 값이 담긴 부분을 추출합니다.
        humi = data["main"]["humidity"]  # 전체 변환된 날씨 데이터 중에서 현재 '습도' 값이 담긴 부분을 추출합니다.

        msg = '    기온은 ' + str(int(temp)) + ' 도 습도는 ' + str(humi) + '퍼센트 입니다.'  # 소수점 기온을 정수로 바꾸고 습도 값과 결합하여 안내할 한글 문장을 완성합니다.
        print(msg)  # 모니터 화면(터미널 창)에 완성된 날씨 안내 문장을 텍스트로 출력합니다.
        option = '-s 180 -p 50 -a 200 -v ko+f5'  # espeak 엔진의 말하기 속도(180), 음높이(50), 볼륨(200), 한국어 여성 목소리(ko+f5) 옵션을 지정합니다.
        speak(option, msg)  # 위에서 지정한 음성 옵션과 날씨 안내 문장을 전달하여 스피커로 소리가 나게 합니다.
        time.sleep(10.0)  # 서버 과부하를 방지하고 주기적인 확인을 위해 다음 실행까지 10초 동안 프로그램을 대기시킵니다.

except KeyboardInterrupt:  # 사용자가 키보드로 'Ctrl + C'를 입력하여 프로그램을 강제로 종료했을 때를 감지합니다.
    pass  # 추가적인 에러 메시지를 출력하지 않고 안전하게 반복문을 빠져나가며 프로그램을 종료합니다.