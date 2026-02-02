#!/usr/bin/env python3
"""네이버 지도 음식점 메뉴 크롤러"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def crawl_menu(restaurant_name):
    """음식점 메뉴를 크롤링하여 출력"""

    # ChromeDriver 자동 설정
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 브라우저 창 숨김
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print(f"\n'{restaurant_name}' 검색 중...")

        # Naver Map 열기
        driver.get("https://map.naver.com/v5/")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "input_search"))
        )

        # 검색어 입력
        search_box = driver.find_element(By.CLASS_NAME, "input_search")
        search_box.send_keys(restaurant_name)
        search_box.send_keys(Keys.RETURN)

        # iframe 로드 대기
        time.sleep(5)
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

        print(f"\n{'='*50}")
        print(f" {restaurant_name} 메뉴")
        print(f"{'='*50}\n")

        for item in menu_items:
            # 메뉴명
            menu_name = item.find_element(By.CSS_SELECTOR, ".lPzHi").text

            # 대표 여부
            is_representative = "⭐ 대표" if item.find_elements(By.CSS_SELECTOR, ".place_blind") else ""

            # 메뉴 설명
            try:
                description = item.find_element(By.CSS_SELECTOR, ".kPogF").text
            except:
                description = ""

            # 가격
            try:
                price = item.find_element(By.CSS_SELECTOR, ".GXS1X em").text
            except:
                price = "가격 정보 없음"

            # 출력
            print(f"  {menu_name} {is_representative}")
            if description:
                print(f"    {description}")
            print(f"    {price}원")
            print()

        print(f"{'='*50}")

    except Exception as e:
        print(f"에러 발생: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    restaurant = input("음식점명을 입력하세요: ")
    if restaurant.strip():
        crawl_menu(restaurant.strip())
    else:
        print("음식점명을 입력해주세요.")