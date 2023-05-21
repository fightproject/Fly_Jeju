# Fly_Jeju

## ✅개발환경 및 기술  
|기술|소개|
|--------|-------|
|Back-End|Python, SQL|
|Database|Bigquery|
|Version Control|Github, Git|
|BI Tool|Looker Studio|
|project personnel|4인 프로젝트|

## ✅여행 경비 정보 웹 서비스 - Travel Expense Information Web Service

## ✅데이터 소개
* 네이버 항공권, 네이버 호텔 홈페이지 크롤링하여 수집(selenium).
* 윈도우 스케줄링을 사용하여 2시간마다 데이터 업데이트 자동화.
* 네이버 항공권: ???? rows × 9 columns

<br>

|columns|Dtype|
|--------|-------|
|date|DATE|
|day|STRING|
|name|STRING|
|airport|STRING|
|leavetime|INTEGER|
|reachtime|INTEGER|
|leavehour|INTEGER|
|seat|STRING|
|charge|INTEGER|

* 네이버 호텔 : ???? rows × 5 columns

<br>

|columns|Dtype|
|--------|-------|
|name|STRING|
|address|STRING|
|rating|STRING|
|star|INTEGER|
|price|INTEGER|


## ✅파이프라인   
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fe7353b7-ab35-4f1c-8854-bc122645451c/Untitled.png)

## ✅대시보드

## ✅결론 및 개선사항
