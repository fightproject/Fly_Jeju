## ✅개발환경 및 기술
|기술|소개|
|--------|-------|
|Back-End|Python, SQL, Flask|
|Front-end|HTML, Bootstrap, CSS, Javascript|
|Database|BigQuery|
|Version Control|Github, Git|
|BI Tool|Looker Studio|
|Project personnel|4인 프로젝트|

<br>

## ✅김포-제주 극성수기 여행 경비 안내 웹 개발- Fly_jeju
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
