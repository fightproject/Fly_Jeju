import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd


def hotelCrawl(URL): # 크롤링 함수
    driver.get(URL)

    time.sleep(5) 

    for c in range(60): # 정해진 횟수 만큼 Page down을 누른다.
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    names = driver.find_elements(By.CLASS_NAME, 'Detail_title__40_dz') # 숙소 이름
    locations = driver.find_elements(By.CLASS_NAME, 'Detail_location__u3_N6') # 숙소 지역
    scores = driver.find_elements(By.CLASS_NAME, 'Detail_score__UxnqZ') # 평점
    charges = driver.find_elements(By.CLASS_NAME, 'Price_show_price__iQpms') # 가격

    # 수정 중

    # for i in range(0, len(leave_reach_Times), 2): #leave_reach_Times에는 출발시간, 도착시간, 출발시간 ... 순으로 들어있기 때문에 두개씩 나눠서 다시 저장
    #     leave_reach_Times_processed.append([leave_reach_Times[i].text, leave_reach_Times[i+1].text])


    # seatTypes_processed = []
    # indexlst = []
    # for k in range(0, len(seatTypes)): # 필요 없는 정보(네이버 할인 정보)를 삭제
    #     seatType = seatTypes[k].text
    #     if '네이버' in seatType:
    #         indexlst.append(k)
    #     else:
    #         seatTypes_processed.append(seatType)

    # charges_processed = []
    # for j in range(len(charges)): # 필요 없는 정보(네이버 할인 가격)를 삭제
    #     if j in indexlst:
    #         continue
    #     else:
    #         charges_processed.append(charges[j].text)

    # result = []
    # for name, lrtime, seat, charge in zip(names, leave_reach_Times_processed, seatTypes_processed, charges_processed):
    #     result.append([name.text, lrtime[0], lrtime[1], seat, charge])

    # return result




# 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless') # 화면 출력 없이 작업
options.add_argument("no-sandbox")
options.add_argument('--ignore-certificate-errors') # 인증서 관련 에러 무시
options.add_argument("--ignore-ssl-errors")
options.add_argument('window-size=1920x1080') # 브라우저 윈도우 사이즈
options.add_argument("disable-gpu") # gpu 가속 사용 x

df = pd.DataFrame(columns=['name', 'leavetime', 'reachtime', 'seat', 'charge', 'date']) # 저장 데이터프레임

# 로드
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options) # 드라이버 위치 경로


baseURL = 'https://hotels.naver.com/list?placeFileName=place%3AJeju_Province&adultCnt=1&includeTax=false&sortField=minRate&sortDirection=ascending&pageIndex=0' # 빠른 테스트용
# 최저가 기준 정렬, page인덱스가 추가 될 수록 페이지가 넘어간다.

for index in range(0, 10):
    goURL = f'https://hotels.naver.com/list?placeFileName=place%3AJeju_Province&adultCnt=1&includeTax=false&sortField=minRate&sortDirection=ascending&pageIndex={index}'
    # goURL = one_wayURL()
    datas = crawl(goURL)

    for data in datas:
        data.append(asdf)
        df.loc[len(df)] = data
        
    print(asdf,'데이터 완료')

driver.quit() # driver 종료

# 데이터 처리

df['charge'] = df['charge'].str.replace(',', '').astype('int')
df['leavetime'] = df['leavetime'].str.replace(':', '').astype('int')
df['reachtime'] = df['reachtime'].str.replace(':', '').astype('int')
print(df)


# from google.cloud import bigquery
# from google.oauth2 import service_account

# # 서비스 계정 인증 정보가 담긴 JSON 파일 경로
# KEY_PATH = "./config/fightproject-8809f75d4a86.json"
# # Credentials 객체 생성
# credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
# # 빅쿼리 클라이언트 객체 생성
# client = bigquery.Client(credentials = credentials, project = credentials.project_id)

# # 테이블 ID
# table_id = "fightproject.test_db.crawltest"

# # 테이블 삭제
# table = client.get_table(table_id)
# client.delete_table(table)

# # 스키마 객체 생성
# schema = [
#     bigquery.SchemaField("name", "STRING", mode="NULLABLE"),
#     bigquery.SchemaField("leavetime", "INTEGER", mode="NULLABLE"),
#     bigquery.SchemaField("reachtime", "INTEGER", mode="NULLABLE"),
#     bigquery.SchemaField("seat", "STRING", mode="NULLABLE"),
#     bigquery.SchemaField("charge", "INTEGER", mode="NULLABLE"),
#     bigquery.SchemaField("date", "INTEGER", mode="NULLABLE")
# ]
# # 테이블 객체 생성
# table = bigquery.Table(table_id, schema=schema)
# # 테이블 생성
# table = client.create_table(table)


# # 테이블 객체 생성
# table = client.get_table(table_id)
# # 데이터프레임을 테이블에 삽입
# client.load_table_from_dataframe(df, table)