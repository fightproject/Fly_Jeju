import glob
from google.cloud import bigquery
from google.oauth2 import service_account
import os
import pandas as pd

def bigqueryCall(sql_input):
        
    # 서비스 계정 키 JSON 파일 경로
    key_path = glob.glob("./app/config/*.json")[0]

    # Credentials 객체 생성
    credentials = service_account.Credentials.from_service_account_file(key_path)
    
    # GCP 클라이언트 객체 생성
    client = bigquery.Client(credentials = credentials, 
                            project = credentials.project_id)

    # 데이터 조회 쿼리
    sql = f'{sql_input}'

    # 데이터 조회 쿼리 실행 결과
    query_job = client.query(sql)

    # 데이터프레임 변환
    df = query_job.to_dataframe()
    # print(df)
    return df
