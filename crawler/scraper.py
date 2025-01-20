from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver 설정
service = Service("/opt/homebrew/bin/chromedriver")
options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome()

try:
    # Naver Map 열기
    driver.get("https://map.naver.com/v5/")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "input_search"))
    )

    # 검색어 입력
    search_box = driver.find_element(By.CLASS_NAME, "input_search")
    search_box.send_keys("후라토식당 잠실직영점")  # 상호명 입력
    search_box.send_keys(Keys.RETURN)

    # iframe 로드 대기 및 출력
    time.sleep(5)  # 초기 로딩 대기
    #디버깅
    # frames = driver.find_elements(By.TAG_NAME, "iframe")
    # print(f"발견된 iframe 개수: {len(frames)}")
    # for i, frame in enumerate(frames):
    #     print(f"Frame {i}: {frame.get_attribute('id')} {frame.get_attribute('name')}")

    # 첫 번째 iframe으로 전환 (디버깅)
    # if frames:
    #     driver.switch_to.frame(frames[0])
    #     print("iframe 전환 성공")
    # else:
    #     print("iframe이 발견되지 않았습니다.")

    driver.switch_to.frame("entryIframe")

    # menu tab click
    menu_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='메뉴']"))
    )
    menu_tab.click()

    # 메뉴 항목 크롤링
    menu_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".E2jtL"))
    )

    for item in menu_items:
        # 메뉴명
        menu_name = item.find_element(By.CSS_SELECTOR, ".lPzHi").text

        # 대표 여부
        is_representative = "대표" if item.find_elements(By.CSS_SELECTOR, ".place_blind") else "일반"

        # 메뉴 설명
        description = item.find_element(By.CSS_SELECTOR, ".kPogF").text

        # 가격
        price = item.find_element(By.CSS_SELECTOR, ".GXS1X em").text

        # 출력
        print(f"메뉴명: {menu_name}")
        print(f"대표: {is_representative}")
        print(f"설명: {description}")
        print(f"가격: {price}원")
        print("-" * 30)

except Exception as e:
    print(f"에러 발생: {e}")

finally:
    input("\n스크래핑 완료. 브라우저를 닫으려면 Enter를 누르세요...")
    driver.quit()