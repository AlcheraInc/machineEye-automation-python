import datetime
import time

from behave import *

from base.BasePage import BasePage
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
import utilities.CustomLogger as cl
import pages.PersonalInfo as pi

from features.environment import get_device_info
import pages.iOS_Elements as ie
import pages.And_Elements as ae
import time

# 연결된 기기에 따라 참고할 xpath 파일 선택
if(get_device_info()[0]=="Android"):
    ce = ae
else:
    ce = ie

logger = cl.custom_logger()

class MachinEyeTest:

    @given("기초설정 + 앱 진입하기")
    def class_objects(context):

        # bdd
        context.mp = MainPage(context.driver)
        context.bp = BasePage(context.driver)
        context.rp = ResultPage(context.driver)

        # 홈 화면 > 앱 아이콘 선택
        try:
            context.bp.find_element_by_xpath(ce.machineye_app).click()
        except:
            print("앱")


    @when("신분증 촬영 대기하기")
    def class_objects(context):
        context.mp.신분증본인확인_버튼()


    @then("결과값 받아오기")
    def class_objects(context):
        nowdate = context.bp.현재시간()

        # 리포트 txt 파일 생성
        f = open("reports/"+nowdate+".txt", "w+")

        # 비교할 데이터 아래 두줄에 변경 필요 #
        check_license = pi.p1_driver
        check_id = pi.p1_id

        f.write(nowdate + "/" + check_license[1] + "/테스트기록 \n")

        for i in range(2):
            context.mp.신분증본인확인_버튼().click()
            start_time = time.time()
            # 면허정보가 없으면 > 주민등록증
            if (context.bp.find_element_by_xpath(ce.driver_result_cnum) == -1):
                f.write("\n*** 주민등록증 / " + str(i + 1) + "번째 시도 ***\n")
                end_time = time.time()
                sec = f"{end_time - start_time:.4f} sec"

                f.write("수행시간 : " + sec + "\n")

                # 결과화면에서 결과값 받아오기
                context.bp.checkOCR(f, "진위여부", context.rp.id_result_assert(), check_id[0])

                context.bp.checkOCR(f, "이름", context.rp.id_result_name(), check_id[1])

                context.bp.checkOCR(f, "주민번호", context.rp.id_result_hnum(), check_id[2])

                context.bp.checkOCR(f, "발급일자", context.rp.id_result_date(), check_id[3])

                context.bp.checkOCR(f, "발행처", context.rp.id_result_from(), check_id[4])

                context.rp.id_result_ok().click()

            # 면허정보가 있으면 (-1 이 아니면) 운전면허증
            else:
                end_time = time.time()
                f.write("\n*** 운전면허증 / " + str(i + 1) + "번째 시도 ***\n")
                sec = f"{end_time - start_time:.4f} sec"

                f.write("수행시간 : " + sec + "\n")
                # 결과화면에서 결과값 받아오기
                context.bp.checkOCR(f, "진위여부", context.rp.driver_result_assert(), check_license[0])

                context.bp.checkOCR(f, "이름", context.rp.driver_result_name(), check_license[1])

                context.bp.checkOCR(f, "주민번호", context.rp.driver_result_hnum(), check_license[2])

                context.bp.checkOCR(f, "발급일자", context.rp.driver_result_date(), check_license[3])

                context.bp.checkOCR(f, "발행처", context.rp.driver_result_from(), check_license[4])

                context.bp.checkOCR(f, "면허타입", context.rp.driver_result_type(), check_license[5])

                context.bp.checkOCR(f, "면허번호", context.rp.driver_result_cnum(), check_license[6])

                context.bp.checkOCR(f, "시리얼번호", context.rp.driver_result_snum(), check_license[8])

                context.rp.driver_result_ok().click()







