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

## ✅서비스 구성 및 제작 과정, 문제점

#### DB 선정
* 오라클 클라우드 DB 생성했지만, 팀원들의 클라우드 계정 생성 불가로 DB 변경.
* 데이터 양이 많을때 강점이 있지만, 분석과 운영이 쉬우며 파이썬과 간단하게 연동할 수 있기에 ```Google BigQuery``` 선정.

#### 데이터 크롤링
* ```selenium``` 을 통한 동적 웹페이지 크롤링
(데이터의 자세한 내용은 위의 데이터 소개 참고)
* 크롤링한 데이터는 데이터 프레임 형식으로 저장.

#### BigQuery와 Python 연동, 데이터 적재.
* google-cloud-bigquery를 사용하여 연동 및 적재.
* Google BigQuery 서비스 계정의 키를 발급받고, Credentials,GCP 클라이언트 객체 생성 후 Bigquery 테이블에 적재.

#### 데이터 수집 자동화
* API를 사용하는 것이 아니기 때문에 실시간으로 반영하기 어렵다는 문제점 발생.
* 항공권의 가격은 실시간으로 변동되기 때문에 윈도우에 기본적으로 있는 작업 스케줄러 사용.
* 작업 스케줄러는 지정한 파일을 지정된 시간에 자동으로 실행하는 프로그램으로 파이썬 코드를 실행 파일로 변환하여 지정했고, 매일 일정 시간마다 실행 가능.

#### 웹서버 구축과 페이지 구현
* 필요한 기능을 선택적으로 확장하거나 추가할 수 있고 프로젝트의 크기와 요구 사항에 맞게 유연하게 사용할 수 있기 때문에 Flask를 사용하여 웹서버 구축.
* Bootstrap 템플릿을 활용하여 페이지의 레이아웃과 디자인을 구성
* 플라스크와 Jinja2 템플릿 엔진을 사용하여 파이썬과 부트스트랩을 연동하여 동적인 웹 페이지를 구현

#### 달력페이지(메인페이지)
* 항공권의 일일 최저, 평균, 최고가에 대한 정보와 날짜 클릭 시 해당 날짜에 대한 데이터를 볼 수 있도록 페이지 이동.
* 달력 구현을 위해 JavaScript와 JavaScript 라이브러리인 FullCalendar 사용.
* Ajax로 DB를 json형식으로 받아와 Javscript 객체로 파싱한 후 서버로부터 날짜 별 항공권 최저가, 최고가, 평균가 정보 받아와서 달력 위에 출력.
![image](https://github.com/KIMJEONGSU/Travel_Expense_Information_Web_Developm/assets/23291338/e7548136-c010-47d1-919b-d3f83525bf95)


#### 목록페이지(항공권, 호텔, 렌터카)
* 달력을 통해서 목록페이지에 이동이 가능하지만 직접 접근하는 경우 기본적으로 7월 1일자의 항공권 목록과 호텔, 렌터카 목록을 가격 오름차순으로 보여줌으로써 최저가를 빠르게 찾을 수 있도록 구성.
* 항공권 목록 : 날짜, 가격범위, 출발지 중 원하는 옵션을 선택하면 HTML form이라는 것을 통해 서버로 전달되고, Flask는 전달된 값을 기반으로 BigQuery Database에 Query를 수행하여 조건에 맞는 데이터를 가져옴.
* Query는 선택된 옵션을 조건으로 BigQuery에서 데이터를 검색하고, 검색결과를 다시 Flask로 전달하여 웹 페이지에 동적으로 출력.
* 호텔목록 : 항공권 목록과 동일한 방식
* 렌터카 목록 : 할인가를 기준으로 오름차순 정렬하여 보여줌.
* 여행경비 총합 기능 : 항공권, 호텔, 렌터카에 대한 항목을 선택하게 되면 Javascript와 이벤트 리스너로 인해 여행 경비 총합을 계산하여 사용자에게 정보 제공.

#### 대시보드 (내부 직원용)



































