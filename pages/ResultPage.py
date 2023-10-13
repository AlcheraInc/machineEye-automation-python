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

class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def cnum_isExist(self):
        return BasePage.isElementExist(self, ce.driver_result_cnum)



    # driver #
    def driver_result_title(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_title)

    def driver_result_assert(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_assert)
    def driver_result_name(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_name)

    def driver_result_hnum(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_hnum)

    def driver_result_from(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_from)

    def driver_result_date(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_date)

    def driver_result_type(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_type)

    def driver_result_cnum(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_cnum)

    def driver_result_snum(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_snum)

    def driver_result_ok(self):
        return BasePage.find_element_by_xpath(self, ce.driver_result_ok)

    # id #
    def id_result_assert(self):
        return BasePage.find_element_by_xpath(self, ce.id_result_assert)

    def id_result_name(self):
        return BasePage.find_element_by_xpath(self, ce.id_result_name)

    def id_result_hnum(self):
        return BasePage.find_element_by_xpath(self, ce.id_result_hnum)

    def id_result_date(self):
        return BasePage.find_element_by_xpath(self, ce.id_result_date)

    def id_result_from(self):
        return BasePage.find_element_by_xpath(self, ce.id_result_from)

    def id_result_ok(self):
        return BasePage.find_element_by_xpath(self, ce.id_result_ok)



