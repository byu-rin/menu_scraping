from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.DEBUG)

# ChromeDriver path (Service)
service = Service("/opt/homebrew/bin/chromedriver")
# add ChromeOptions
options = webdriver.ChromeOptions()
# init WebDriver
driver = webdriver.Chrome(service=service, options=options)

# input store name from user
# store_name = input("검색할 상호명을 입력하세요 : ")
# enter chrome driver

# open naver map
driver.get("https://map.naver.com/v5/")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "input_search"))
)
time.sleep(5)  # 초기 로딩 대기


    # search store name
search_box = driver.find_element(By.CLASS_NAME, "input_search")
search_box.send_keys("후라토식당 잠실직영점")  # 상호명 입력
search_box.send_keys(Keys.RETURN)  # 검색 실행
try:
    # # 프레임 로드 대기
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "entryIframe"))
    # )
    # driver.switch_to.frame("entryIframe")
    
     # waiting until search result
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".search_result"))
    )

    menu_tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "메뉴"))
    )
    menu_tab.click()

except Exception as e:
    print(f"error: {e}")

finally:
    # 브라우저 종료
    input("\n스크래핑 완료. 브라우저를 닫으려면 Enter를 누르세요...")
    driver.quit()