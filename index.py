#불러올 라이브러리
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#주제 물음
subject = input("검색:")

#옵션 정의
chrome_options = Options()

chrome_options.add_argument("headless")
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--disable-loging')

#웹 열기
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.hani.co.kr/")

#검색창에 주제 insert
search_box = driver.find_element(By.NAME, 'searchword')
search_box.send_keys(subject)
search_box.send_keys(Keys.RETURN)

#최상단 뉴스 제목, url 가져오기
search_1 = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(2) > div > h4 > a').text
search_1_href = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(2) > div > h4 > a').get_attribute('href')
search_2 = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(3) > div > h4 > a').text
search_2_href = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(3) > div > h4 > a').get_attribute('href')
search_3 = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(4) > div > h4 > a').text
search_3_href = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(4) > div > h4 > a').get_attribute('href')
search_4 = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(5) > div > h4 > a').text
search_4_href = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(5) > div > h4 > a').get_attribute('href')
search_5 = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(6) > div > h4 > a').text
search_5_href = driver.find_element(By.CSS_SELECTOR, '#section-left-scroll-in > div.search-list.section-list-area > div:nth-child(6) > div > h4 > a').get_attribute('href')

#결과값 프린트
print("1. " + search_1 + "  " + search_1_href)
print("2. " + search_2 + "  " + search_2_href)
print("3. " + search_3 + "  " + search_3_href)
print("4. " + search_4 + "  " + search_4_href)
print("5. " + search_5 + "  " + search_5_href)

driver.close()