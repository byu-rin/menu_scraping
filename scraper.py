from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 사용자로부터 상호명 입력 받기
store_name = input("검색할 상호명을 입력하세요 : ")

# 크롬 드라이버 실행
driver = webdriver.Chrome()

# 네이버 지도 열기
driver.get("https://map.naver.com/")
time.sleep(5) # 페이지 로딩 대기 (필요 시 조정)

# 검색창에 상호명 입력
search_box = driver.find_element(By.CLASS_NAME, "input_search")
search_box.send_keys("스타벅스") # 검색할 상호명 입력
time.sleep(1) # 대기 (필요 시 추가)

# 검색 (enter 키 누르기)
search_box.send_keys(Keys.RETURN)  # Keys.RETURN 또는 Keys.ENTER 사용
time.sleep(5)  # 검색 결과 로딩 대기

# 사용자가 Enter를 누를 때까지 대기
input("브라우저를 닫으려면 Enter를 누르세요...")

# 브라우저 종료
driver.quit()