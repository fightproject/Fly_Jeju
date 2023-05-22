from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd


start = time.time()

options = webdriver.ChromeOptions()
options.add_argument('headless') # 화면 출력 없이 작업
options.add_argument("no-sandbox")
options.add_argument('--ignore-certificate-errors') # 인증서 관련 에러 무시
options.add_argument("--ignore-ssl-errors")
options.add_argument('window-size=1920x1080') # 브라우저 윈도우 사이즈
options.add_argument("disable-gpu") # gpu 가속 사용 x


df = pd.DataFrame(columns=['name', 'address', 'rating', 'star', 'price']) # 저장 데이터프레임

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
for page_num in range(60): #페이지 넘기기, 60 이후로 조회 가격이 없다.
    url = f'https://hotels.naver.com/list?placeFileName=place%3AJeju_Province&adultCnt=1&includeTax=false&sortField=popularityKR&sortDirection=descending&pageIndex={page_num}'
    driver.get(url)
    time.sleep(2)

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
            hotel_data = [hotel_name, hotel_address, hotel_rating, hotel_star, hotel_price]
            df.loc[len(df)] = hotel_data

        except:
            hotel_data = [hotel_name, hotel_address, hotel_rating, None, hotel_price]
            df.loc[len(df)] = hotel_data
    print('현재 페이지 :', page_num)


# 데이터 처리
df['star'] = df['star'].fillna(-1).astype('int').replace({-1: None})
df['price'] = df['price'].astype('int')


print(df)


from google.cloud import bigquery
from google.oauth2 import service_account

# 서비스 계정 인증 정보가 담긴 JSON 파일 경로
KEY_PATH = "./config/fightproject-8809f75d4a86.json"
# Credentials 객체 생성
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
# 빅쿼리 클라이언트 객체 생성
client = bigquery.Client(credentials = credentials, project = credentials.project_id)

# 테이블 ID
# table_id = "fightproject.test_db.hoteltest" # 테스트 용
table_id = "fightproject.test_db.hotelcrawl" # 실제 사용

# 테이블 삭제, 첫 DB 생성 땐 주석처리
table = client.get_table(table_id)
client.delete_table(table)

# 스키마 객체 생성
schema = [
    bigquery.SchemaField("name", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("address", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("rating", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("star", "INTEGER", mode="NULLABLE"),
    bigquery.SchemaField("price", "INTEGER", mode="NULLABLE")
]
# 테이블 객체 생성
table = bigquery.Table(table_id, schema=schema)
# 테이블 생성
table = client.create_table(table)


# 테이블 객체 생성
table = client.get_table(table_id)
# 데이터프레임을 테이블에 삽입
client.load_table_from_dataframe(df, table)

# pyarrow가 필요한듯? pip install pyarrow

end = time.time()

print(f"{end - start:.5f} sec")