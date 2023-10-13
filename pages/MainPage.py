from base.BasePage import BasePage
import utilities.CustomLogger as cl
from features.environment import get_device_info
import pages.iOS_Elements as ie
import pages.And_Elements as ae

# 연결된 기기에 따라 참고할 xpath 파일 선택
if(get_device_info()[0]=="Android"):
    ce = ae
else:
    ce = ie


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def 신분증본인확인_버튼(self):
        return BasePage.find_element_by_xpath(self, ce.cardreader_button)