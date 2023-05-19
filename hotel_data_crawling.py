from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

crawling = []
for page_num in range(2):
    driver = webdriver.Chrome('/content/drive/MyDrive/chromedriver_win32')
    url = f'https://hotels.naver.com/list?placeFileName=place%3AJeju_Province&adultCnt=1&includeTax=false&sortField=popularityKR&sortDirection=descending&pageIndex={page_num}'
    driver.get(url)
    time.sleep(1)

    hotel_info = driver.find_element(By.CSS_SELECTOR, 'ul.SearchList_SearchList__CtPf8')
    li_tags = hotel_info.find_elements(By.TAG_NAME, 'li')
    for i in li_tags:
        try:
            # 호텔명
            hotel_name = i.find_element(By.CSS_SELECTOR, 'h4').text

            # 호텔 주소(ex. 서귀포, 대한민국 -> split사용해서 서귀포만 저장)
            temp_hotel_address = i.find_element(By.CSS_SELECTOR, 'i.Detail_location__u3_N6').text
            hotel_address = temp_hotel_address.split(',')[0]

            # 호텔 별점
            hotel_rating = i.find_element(By.CSS_SELECTOR, 'i.Detail_score__UxnqZ').text

            # 호텔 성급 (ex. 5성급 -> 5 만 저장)
            temp_hotel_star = i.find_element(By.CSS_SELECTOR, 'i.Detail_grade__y5BmJ').text
            hotel_star = re.sub('[^0-9]', '', temp_hotel_star)
            
            # 호텔 가격 (ex. 296,000원~ -> 296000 만 저장.)
            temp_hotel_price = i.find_element(By.CSS_SELECTOR, 'em.Price_show_price__iQpms').text
            hotel_price = re.sub('[^0-9]', '', temp_hotel_price)
            time.sleep(1)
            hotel_data = {'호텔이름': hotel_name, '호텔주소': hotel_address, '호텔별점': hotel_rating,'호텔성급': hotel_star, '호텔가격': hotel_price}
            crawling.append(hotel_data)

        except:
            hotel_data = {'호텔이름': hotel_name, '호텔주소': hotel_address, '호텔별점': hotel_rating,'호텔성급': None, '호텔가격': hotel_price}
            crawling.append(hotel_data)


print(crawling)