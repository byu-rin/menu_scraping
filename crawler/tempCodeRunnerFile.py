    # iframe 내부로 이동
    driver.switch_to.frame("entryIframe")  # iframe 이름이 "entryIframe"인 경우
    time.sleep(3)

    # 메뉴 정보 추출
    menu_items = driver.find_elements(By.CSS_SELECTOR, ".menu_list .menu_name")
    if menu_items:
        print(f"\n[{store_name}] 메뉴 정보:")
        for idx, item in enumerate(menu_items, start=1):
            print(f"{idx}. {item.text}")
    else:
        print(f"[{store_name}] 메뉴 정보를 찾을 수 없습니다.")

except Exception as e:
    print(f"오류 발생: {e}")