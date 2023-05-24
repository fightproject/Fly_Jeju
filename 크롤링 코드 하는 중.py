import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd


# 임시 함수 모음

def one_wayURL(): # 편도 URL 함수
    isDomestic = int(input('국내선 : 1, 국외선 : 2\n')) # 1 국내선, 2 국외선을 판단.

    if isDomestic == 1:
        flightKind = 'domestic'
    elif isDomestic == 2:
        flightKind = 'international'
    else:
        print('범위 외의 값입니다.')

    leaveAirport = input('출발 공항\n') # 출발공항 받기
    reachAirport = input('도착 공항\n') # 도착공항 받기

    goTo = input('출발 날짜\n') # 출발날짜 받기

    adult = 'adult='+input('성인 명수\n') # 성인 받기
    child = 'child='+input('소아 명수\n') # 소아 받기
    infant = 'infant='+input('유아 명수\n') # 유아 받기
    fareType = 'fareType='+input('국내 전체 좌석 : YC, 국내 일반 좌석 : Y, 국내 비즈니스석 : C \n') # 좌석정보 받기

    return f'{base_URL}/{flightKind}/{leaveAirport}-{reachAirport}-{goTo}?{adult}&{child}&{infant}&{fareType}'

def two_wayURL(): # 왕복(편도+편도)URL 만드는 함수
    isDomestic = int(input('국내선 : 1, 국외선 : 2\n')) # 1 국내선, 2 국외선을 판단.

    if isDomestic == 1:
        flightKind = 'domestic'
    elif isDomestic == 2:
        flightKind = 'international'
    else:
        print('범위 외의 값입니다.')

    leaveAirport = input('출발 공항\n') # 출발공항 받기
    reachAirport = input('도착 공항\n') # 도착공항 받기

    goTo = input('출발 날짜\n') # 출발날짜 받기
    backTo = input('귀환 날짜\n') # 귀환날짜 받기

    adult = 'adult='+input('성인 명수\n') # 성인 받기
    child = 'child='+input('소아 명수\n') # 소아 받기
    infant = 'infant='+input('유아 명수\n') # 유아 받기
    fareType = 'fareType='+input('국내 전체 좌석 : YC, 국내 일반 좌석 : Y, 국내 비즈니스석 : C \n') # 좌석정보 받기

    return f'{base_URL}/{flightKind}/{leaveAirport}-{reachAirport}-{goTo}?{adult}&{child}&{infant}&{fareType}', f'{base_URL}/{flightKind}/{reachAirport}-{leaveAirport}-{backTo}?{adult}&{child}&{infant}&{fareType}'

def crawl(URL): # 크롤링 함수
    driver.get(URL)

    time.sleep(5) 

    for c in range(60): # 정해진 횟수 만큼 Page down을 누른다.
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    names = driver.find_elements(By.CLASS_NAME, 'name') # 공항 이름
    leave_reach_Times = driver.find_elements(By.CLASS_NAME, 'route_time__-2Z1T') # 출발 시간, 도착 시간
    seatTypes = driver.find_elements(By.CLASS_NAME, 'domestic_type__30RSq') # 좌석 타입
    charges = driver.find_elements(By.CLASS_NAME, 'domestic_num__2roTW') # 가격

    leave_reach_Times_processed = []

    for i in range(0, len(leave_reach_Times), 2): #leave_reach_Times에는 출발시간, 도착시간, 출발시간 ... 순으로 들어있기 때문에 두개씩 나눠서 다시 저장
        leave_reach_Times_processed.append([leave_reach_Times[i].text, leave_reach_Times[i+1].text])


    seatTypes_processed = []
    indexlst = []
    for k in range(0, len(seatTypes)): # 필요 없는 정보(네이버 할인 정보)를 삭제
        seatType = seatTypes[k].text
        if '네이버' in seatType:
            indexlst.append(k)
        else:
            seatTypes_processed.append(seatType)

    charges_processed = []
    for j in range(len(charges)): # 필요 없는 정보(네이버 할인 가격)를 삭제
        if j in indexlst:
            continue
        else:
            charges_processed.append(charges[j].text)

    result = []
    for name, lrtime, seat, charge in zip(names, leave_reach_Times_processed, seatTypes_processed, charges_processed):
        result.append([name.text, lrtime[0], seat, charge]) # 적재 테스트 때문에 출발 시간에 [0] 붙였음

    return result

df = pd.DataFrame(columns=['name', 'time', 'seat', 'charge']) # 저장 데이터프레임

# 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless') # 화면 출력 없이 작업
options.add_argument("no-sandbox")
options.add_argument('--ignore-certificate-errors') # 인증서 관련 에러 무시
options.add_argument("--ignore-ssl-errors")
options.add_argument('window-size=1920x1080') # 브라우저 윈도우 사이즈
options.add_argument("disable-gpu") # gpu 가속 사용 x

# 로드
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options) # 드라이버 위치 경로

base_URL = 'https://flight.naver.com/flights'

isOne_Way = int(input('편도 : 1, 왕복 : 2\n'))

goURL = 'https://flight.naver.com/flights/domestic/GMP-CJU-20230601?adult=1&fareType=YC' # 빠른 테스트용


if isOne_Way == 1:
    for asdf in range(1,6):
        goURL = f'https://flight.naver.com/flights/domestic/GMP-CJU-2023070{asdf}?adult=1&fareType=YC'
        # goURL = one_wayURL()
        datas = crawl(goURL)

        for i in range(len(datas)):
            df.loc[i] = datas[i]
            print(datas[i])

    driver.quit() # driver 종료

elif isOne_Way == 2: # 아직 테스트 안해봄
    goURL, backURL = two_wayURL()
    goDatas = crawl(goURL)
    backDatas = crawl(backURL)


    for goData in goDatas:
        print(goData)
    
    for backData in backDatas:
        print(backData)

    driver.quit() # driver 종료

else:
    print('범위 외의 값 입니다.')


from google.cloud import bigquery
from google.oauth2 import service_account

# 서비스 계정 인증 정보가 담긴 JSON 파일 경로
KEY_PATH = "./config/fightproject-8809f75d4a86.json"
# Credentials 객체 생성
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
# 빅쿼리 클라이언트 객체 생성
client = bigquery.Client(credentials = credentials, project = credentials.project_id)

# 테이블 ID
table_id = "fightproject.test_db.crawltest"

# 테이블 삭제
table = client.get_table(table_id)
client.delete_table(table)

# 스키마 객체 생성
schema = [
    bigquery.SchemaField("name", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("time", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("seat", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("charge", "STRING", mode="NULLABLE")
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
