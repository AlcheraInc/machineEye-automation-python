import base64
import os
import subprocess
from appium import webdriver
import time


import utilities.CustomLogger as cl

logger = cl.custom_logger()
BASE_DIR = os.getcwd()
URL = 'http://127.0.0.1:4723/wd/hub'
# apps = 'FaceSDKProSample.ipa' # for iOS
# app = os.path.join(BASE_DIR, 'apps', apps)
#
# print("baseDir = " + BASE_DIR)
# print("app = " + app)

# 현재 연결된 기기 정보를 받아오는 함수
def get_device_info():
    # ADB 명령어 실행
    cmd = 'adb devices'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    os = ''
    divice_info = ''
    info = []

    # 출력 결과를 파싱하여 모바일 기기 정보 추출
    lines = out.decode().splitlines()
    print("adb devices ", len(lines))

    if(len(lines) >= 3):
        print("Android 연결 상태")
        os = 'Android'
        divice_info = lines[1].split()
        print("안드 정보 : ", divice_info[0])

        # info 배열에 os / udid / "deviceName" 담기
        info = [os, divice_info[0], "deviceName"]

    else:
        print("*** iOS 연결 상태 ***")
        cmd = 'xctrace list devices'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()

        lines = out.decode().splitlines()
        print("xctrace list devices ", len(lines))

        os = 'ios'

        for i in range(len(lines)):
            divice_info = lines[i].split()
            print(divice_info)

            # 첫번째 줄 Pass ( == Devices == )
            if(i==0):
                continue

            # 공백인 경우 Pass
            if(len(divice_info)==0):
                continue


            device_name = divice_info[0]
            udid = divice_info[len(divice_info)-1].strip("("")")

            udid_len = udid.split("-")
            if len(udid_len) == 1 or len(udid_len) == 2:
                print("iOS 정보 : ", udid)

                # info 배열에 os / udid / device_name 담기
                info = [os, udid, device_name]
                break
            else:
                continue

    # os / udid / device_name 정보가 담긴 info 리턴
    return info



def before_feature(context, feature):

    # 현재 연결된 정보 받아오기
    info = get_device_info()
    print("함수 결과", info[0], info[1])

    # dl
    if (info[0] == "Android"):
        capabilities = {
            "platformName": info[0],
            'automationName': 'uiautomator2',
            "appium:udid": info[1]
        }
    else:
        capabilities = {
            "platformName": info[0],
            'deviceName': info[2],
            "appium:automationName": "XCUITest",
            "appium:udid": info[1]
        }


    context.driver = webdriver.Remote(command_executor=URL, desired_capabilities=capabilities)


def after_feature(context,feature):
    # stop_recoding(context)
    context.driver.quit()

