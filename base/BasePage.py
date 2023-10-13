import os

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import utilities.CustomLogger as log
import time

from traceback import print_stack
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import WebElement

waitTime = 10
BASE_DIR = os.getcwd()
logger = log.custom_logger()


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def save_screen_shot_tofile(self):
        image_file_name = f'{time.strftime("%Y%m%d_%H%M%S")}_.png'
        image_file_path = os.path.join(BASE_DIR + "/reports", image_file_name)
        self.driver.save_screenshot(image_file_path)
        logger.info(f'{image_file_path} saved')

    def is_exist(self, locator):
        elemList = self.driver.find_elements(By.XPATH, locator)
        if (len(elemList) == 0):
            print("***" + locator + " 확인 불가 ")
        else:
            print("***" + locator + " 확인! ")

        return len(elemList)

    def take_screenshotoallure(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def is_displayed(self, locator):
        self.driver.implicitly_wait(waitTime)
        try:
            self.driver.find_element(by=AppiumBy.XPATH, value=locator).is_displayed()
            self.take_screenshotoallure(locator)
            logger.info("Displayed locator value " + locator)
            return True
        except NoSuchElementException:
            print_stack()
            logger.info("No Displayed locator value " + locator)
            self.take_screenshotoallure(locator)
            self.save_screen_shot_tofile()
            return False

    def click_elements_by_xpath(self, locator):
        self.driver.implicitly_wait(waitTime)
        try:
            el = self.driver.find_element(by=AppiumBy.XPATH, value=locator)
            self.take_screenshotoallure(locator)
            el.click()
        except NoSuchElementException:
            print_stack()
            logger.info(
                "Unable to Click with locator value " + locator)
            self.take_screenshotoallure(locator)
            self.save_screen_shot_tofile()
            assert False

    # xpath에 해당하는 element를 찾는 함수 (없는 경우 -1 반환)
    def find_element_by_xpath(self, locator):
        try:
            self.driver.implicitly_wait(waitTime)
            el = self.driver.find_element(by=AppiumBy.XPATH, value=locator)

            return el
        except:
            return -1

    # 해당 element 가 attr 속성값을 가지고 있는지 체크하는 함수 (없는 경우 "미표기" 반환)
    def hasAttribute(self, element, attr):
        try:
            tmp = element.get_attribute(attr)
            return tmp
        except:
            return "미표기"


    # xpath에 해당하는 element가 존재하는지 확인하는 함수
    def isElementExist(self, xpath):
        elem = self.find_element_by_xpath(xpath)
        return elem

    def 현재시간(self):
        return time.strftime('%Y-%m-%d %H:%M:%S')

    # PersonalInfo.py 정보와 실제 읽어온 OCR 정보를 비교하는 함수 (레포트에 기록)
    def checkOCR(self, f, col, rp, pi):
        if (rp == -1):
            f.write("X " + col + " : Fail\n")
            f.write(">>> Real : " + pi + " / OCR : 미표기 \n")

        else:
            ocr = self.hasAttribute(rp, "name")
            if (str(ocr).replace(" ","") == pi.replace(" ","")):
                f.write("O " + col + " : Pass\n")
            else:
                f.write("X " + col + " : Fail\n")
                f.write(">>> Real : " + pi + " / OCR : " + str(ocr) + "\n")
