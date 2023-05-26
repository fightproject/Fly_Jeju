## ✅개발환경 및 기술
|기술|소개|
|--------|-------|
|Back-End|Python, SQL, Flask|
|Front-end|HTML, Bootstrap, CSS, Javascript|
|Database|BigQuery|
|Version Control|Github, Git|
|BI Tool|Looker Studio|
|Project personnel|4인 프로젝트|
|project period|2023.05.15~2023.05.26|

<br>

## ✅김포-제주 극성수기 여행 경비 안내 웹 개발- Travel_Expense_Information_Web_Developm
제주도 여행 경비를 고려했을때 고정적으로 발생하는 비용인 항공권, 숙박시설, 렌터카 요금을 합산한 금액을 간단하게 조회해볼 수 없을까 하는 의문과 아직은 항공권, 숙박, 렌터카 요금을 따로 보여주는 웹 서비스만 존재합니다.
또한 조사결과 2030 젊은층은 해외여행을 선호하는 반면, 60대 이상 노년층은 국내에 더 관심많았습니다. 가성비 여행을 찾는 2030 젊은층의 국내 여행 증가를 위해 관광객들에게 저렴한 경비를 보다 편리하고 정확한 정보를 제공할 수 있는 서비스 필요성으로 인해 해당 프로젝트를 진행하게 되었습니다.
국내 여행지 중 항공을 이용하여 여행을 가장 많이 가는 제주와 제주에서 출발하는 운항 중 가장 많은 도착지인 김포공항의 극성수기(7월~8월)로 범위를 선정하였습니다.

<br>

## ✅데이터 소개


* 항공권   
  * 데이터 : 9columns X 22131 rows
  * 출처 : 네이버 항공권 홈페이지

<br>

|Columns|Dtype|
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

<br>
  
* 호텔
  * 데이터 : 5columns X 1200 rows
  * 출처 : 네이버 호텔 홈페이지

<br>

|Columns|Dtype|
|--------|-------|
|name|STRING|
|address|STRING|
|rating|STRING|
|star|INTEGER|
|price|INTEGER|

<br>

* 렌터카
  * 데이터 : 10columns X 8236 rows
  * 출처 : 코드스테이츠

<br>

|Columns|Dtype|
|--------|-------|
|id|INTEGER|
|carname|STRING|
|date|FLOAT|
|day|STRING|
|diltype|STRING|
|seater|INTEGER|
|year|STRING|
|avg_year|INTEGER|
|regular_price|STRING|
|discounted_price|STRING|

<br>

## ✅파이프라인
![image](https://github.com/KIMJEONGSU/Travel_Expense_Information_Web_Developm/assets/23291338/f258c2c6-288a-4db9-9fa0-2957869a288c)

<br>

1. selenium을 사용하여 BigQuery Database에 적재.
2. DB와 Looker Studio 그리고 웹서버 연동.
3. 사용자가 날짜 입력 또는 기타옵션 선택시 URL 호출
4. 호출한 URL로 지정된 뷰함수 호출
5. 호출한 요청을 분석 및 논리 실행
6. 분석결과 응답으로 전송
7. 응답으로 전송할 값을 HTML에 표현.
8. 사용자에게 가격 총합 제공.

<br>

## ✅내부 디렉토리 구조
```
Data
┖ Start.bat
┖ airplaneCrawl0701_0715.py # 항공권데이터 크롤링 코드
┖ airplaneCrawl0716_0731.py # 항공권데이터 크롤링 코드
┖ airplaneCrawl0801_0815.py # 항공권데이터 크롤링 코드
┖ airplaneCrawl0816_0831.py # 항공권데이터 크롤링 코드
┖ chromedriver.exe # 크롬드라이버
┖ hotel_data_crawling.py # 호텔데이터 크롤링 코드
┖ 환경.txt # 윈도우 스케줄링을 위한 환경 설정 설명
app
┖ __pycache__
┖ config
     ┖ fightproject-46d68da728a3.json # Bigquery 서비스 계정 키
┖ static/assets
     ┖ css
     ┖ fonts
     ┖ images
     ┖ js
        ┖ vendor
            ┖ fullcalendar.min.js # js 달력라이브러리
        ┖ pages
            ┖ demo.calendar.js #달력 커스텀 및 데이터 출력
        ┖ filght_total_price.js # 항공권, 호텔, 렌트카 경비 합산
┖ templates
      ┖ dashboard1.html # 데이터 분석 대시보
      ┖ filght.html # 항공권, 호텔, 헨트카 목록 출력
      ┖ main.html # 메인달력, 항공권 최저가, 평균가, 최고가 금액 출력
┖ bigquery.py # 웹서버, DB 연결 코드
┖ main.py # Flask로 app구축, jinja2, bootstrap을 활용하여 페이지 연동
```

<br>

## ✅서비스 구성 및 제작 과정

### DB 선정


































