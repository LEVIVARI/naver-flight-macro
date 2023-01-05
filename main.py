# 라이브러리 임포트
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 드라이버 실행 및 페이지 이동
driver = webdriver.Firefox()
url = "https://flight.naver.com/flights/domestic/GMP-USN-20230119?adult=2&fareType=YC"
driver.get(url)
driver.implicitly_wait(10)
notCheap = True

# refresh method
while notCheap == True:
    driver.refresh()
    sleep(10)
    ticketPrice = driver.find_elements(By.CLASS_NAME, "domestic_num__2roTW")

    for i in range(len(ticketPrice)):
        price = ticketPrice[i].text
        numPrice = int(price.replace(",", ""))
        print(numPrice)
        if numPrice<50000:
            notCheap == False
            print('booking now')