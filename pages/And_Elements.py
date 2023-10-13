
# 홈화면 > Facesdk 앱
facesdk_app = "//XCUIElementTypeIcon[@name='Face SDK Pro Demo']"
machineye_app = '//android.widget.TextView[contains(@content-desc,"MachineEye OCR")]'

# lock 화면
lock = '//XCUIElementTypeWindow[@name="SBCoverSheetWindow"]'

# Main Page
cardreader_button = '//android.widget.Button[contains(@text,"스캔 시작")]'


# Result Page - driver
driver_result_title = '//android.widget.TextView[contains(@resource-id,"alertTitle"]'

driver_result_assert = '//android.widget.TextView[contains(@text,"진위 여부")]/following-sibling::android.widget.TextView[1]'
driver_result_name = '//android.widget.TextView[contains(@text,"이 름")]/following-sibling::android.widget.TextView[1]'
driver_result_hnum = '//android.widget.TextView[contains(@text,"주민번호")]/following-sibling::android.widget.TextView[1]'
driver_result_date = '//android.widget.TextView[contains(@text,"발 행 일")]/following-sibling::android.widget.TextView[1]'
driver_result_from = '//android.widget.TextView[contains(@text,"발 행 처")]/following-sibling::android.widget.TextView[1]'
driver_result_type = '//android.widget.TextView[contains(@text,"면허타입")]/following-sibling::android.widget.TextView[1]'
driver_result_cnum = '//android.widget.TextView[contains(@text,"면허번호")][1]/following-sibling::android.widget.TextView[1]'
driver_result_snum = '//android.widget.TextView[contains(@text,"시 리 얼")][1]/following-sibling::android.widget.TextView[1]'
driver_result_ok = '//android.widget.Button[contains(@text,"OK")]'


# Result Page - id
id_result_assert = '//android.widget.TextView[contains(@text,"진위 여부")]/following-sibling::android.widget.TextView[1]'
id_result_name = '//android.widget.TextView[contains(@text,"이 름")]/following-sibling::android.widget.TextView[1]'
id_result_hnum = '//android.widget.TextView[contains(@text,"주민번호")]/following-sibling::android.widget.TextView[1]'
id_result_date = '//android.widget.TextView[contains(@text,"발 행 일")]/following-sibling::android.widget.TextView[1]'
id_result_from = '//android.widget.TextView[contains(@text,"발 행 처")]/following-sibling::android.widget.TextView[1]'
id_result_ok = '//android.widget.Button[contains(@text,"OK")]'
