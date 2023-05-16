from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time
import numpy as np
import os
import tqdm

def crawing_data(m=2):
    # 데이터 저장할 리스트
    Naver_Flight_Data = []

    # 크롤링할 URL
    for i in tqdm(range(1,m)):
        #m이 10미만이면 01,02,03이런식으로 주소를 불러옴
        if m < 10:
            url = f'https://m-flight.naver.com/flights/domestic/SEL-CJU-2023070{i}?adult=1&fareType=YC'
        # m이 10 이상이면 11,12,13 이런식으로 주소를 불러옴.
        url = f'https://m-flight.naver.com/flights/domestic/SEL-CJU-202307{i}?adult=1&fareType=YC'
        driver.get(url)
        time.sleep(5)

        # # 스크롤러를 끝까지 내리기 위해 페이지의 높이 정보 가져오기
        # page_height = driver.execute_script('return document.documentElement.scrollHeight')

        # # 페이지 끝까지 스크롤 다운
        # while True:
        #     driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
        #     # 스크롤 다운 후 로딩 대기 시간 설정 (필요에 따라 조정 가능)
        #     driver.implicitly_wait(3)
            
        #     # 스크롤 다운 후의 페이지 높이 정보 가져오기
        #     new_page_height = driver.execute_script('return document.documentElement.scrollHeight')
            
        #     # 이전 페이지 높이와 새로운 페이지 높이 비교, 스크롤을 끝까지 내렸다면, 크롤링 시작.
        #     if new_page_height == page_height:
        try:
            flights = driver.find_elements(By.CSS_SELECTOR, '.search_result_list .box_result')

            for flight in flights:
                airline = flight.find_element(By.CSS_SELECTOR, '.info_airline').text
                departure_time = flight.find_element(By.CSS_SELECTOR, '.time_departure .time').text
                arrival_time = flight.find_element(By.CSS_SELECTOR, '.time_arrival .time').text
                departure_city = flight.find_element(By.CSS_SELECTOR, '.airport_departure').text
                arrival_city = flight.find_element(By.CSS_SELECTOR, '.airport_arrival').text
                seat_type = flight.find_element(By.CSS_SELECTOR, '.ticket_type span').text
                price = flight.find_element(By.CSS_SELECTOR, '.txt_price em').text
                duration = flight.find_element(By.CSS_SELECTOR, '.time_total').text

                Naver_Flight_Data_dict = {'항공사': airline,'출발시간': departure_time,'도착시간': arrival_time,
                                            '출발도시': departure_city,'도착도시': arrival_city,
                                            '좌석유형': seat_type,'가격': price,'비행시간': duration}
                Naver_Flight_Data.append(Naver_Flight_Data_dict)
        except:
            break
                        
            time.sleep(5)

    return Naver_Flight_Data

FILEPATH = os.path.join(os.getcwd(), 'chromedriver_win32')
driver = webdriver.Chrome() 
Naver_Flight_Data = crawing_data()
print(Naver_Flight_Data)