from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

def crawling_data():
    crawling = []

    FILEPATH = os.path.join(os.getcwd(), 'chromedriver_win32')
    driver = webdriver.Chrome(FILEPATH)
    url = 'https://hotels.naver.com/'
    driver.get(url)

    time.sleep(15)

    element = driver.find_element(By.ID,'#__next > div > div.popup_travelclub > div > div.btns > button:nth-child(1)')
    element.send_keys(Keys.ENTER)
    # keyword='제주도'

    # element = driver.find_element(By.ID, '#textInput')
    # element.send_keys(keyword)
    # time.sleep(3)
    # element.send_keys(Keys.ENTER)
    # time.sleep(3)
    # driver.find_element(By.CSS_SELECTOR,'#SearchBoxContainer > div.Box-sc-kv6pi1-0.hRUYUu.TabContent__Search--button > button > div > div > span')

crawling_data()