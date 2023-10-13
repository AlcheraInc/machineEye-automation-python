# 구현된 내용
1. machineEye 아이콘이 화면에 보이는 상태에서 실행 필요
2. 실행 시, 연결된 기기(And/iOS)에 따라 자동으로 capabilities 값을 찾고, 그에 맞게 자동화 실행된다. (And+iOS 연결되어있다면 And 우선)
3. 촬영되는 신분증에 맞게 분기처리된다. (운전면허증 / 주민등록증)
4. 10 번을 자동으로 찍으면서 OCR 결과값을 받아오고, report/ 내 txt 에 체크사항이 기입된다.

# 구조
- 테스트 프레임워크 : Appium
- BDD : behave
- 디자인패턴 : PageObject
- Report : allure

# 사전설치 1. Apppium
1. Appium 설치 및 실행
- http://appium.io/docs/en/2.1/quickstart/install/ 참고

2. Appium Driver 설치
```
#Install
npm i --location=global appium
appium driver install uiautomator2
appium driver install xcuitest
#Run
appium --base-path /wd/hub
```
# 사전설치 2 pip
```
pip install -r requirements.txt
```

# 실행
- behave를 통해서 실행해준다.

```
 sh run-behave.sh 
```

