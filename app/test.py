
@app.route('/filght', methods=['GET','POST'])
def get_flight(num=None):
    global total_amount
    car_data = clinet_bigquery('''SELECT  carname, oiltype, seater, avg_year,
                                    CAST(AVG(CAST(regular_price AS INT)) AS INT) AS avg_regular_price,
                                    CAST(AVG(CAST(discounted_price AS INT)) AS INT) AS avg_discounted_price
                                    FROM `fightproject.test_db.car`
                                    WHERE regular_price != '마감' AND discounted_price != '마감'
                                    GROUP BY carname, oiltype, seater, avg_year
                                    ORDER BY avg_discounted_price, avg_regular_price
                                    LIMIT 10;''') 
    # 호텔데이터불러오기(기본)
    hotel_data = clinet_bigquery('''SELECT * FROM test_db.hotelcrawl
                                    where rating != '평점없음' and star is not null
                                    order by star desc, price asc
                                    LIMIT 10;''') 
    
    if request.method=='POST':
        selected_date = request.json.get('date')

        # 항공권과 호텔, 렌터카에 대한 총합 보여주기위함.
        selected_air = request.form.getlist('customCheck1')
        selected_hotels = request.form.getlist('customCheck2')
        selected_car = request.form.getlist('customCheck3')
        total_amount = sum(float(air_data[int(index)]['charge']) for index in selected_air) + \
                    sum(float(hotel_data[int(index)]['price']) for index in selected_hotels) + \
                    sum(float(car_data[int(index)]['avg_discounted_price']) for index in selected_car)

    # 데이터베이스에서 선택된 날짜의 데이터를 가져오는 코드
        sql = f'''
            SELECT date, day, name, airport, leavetime, reachtime, seat,charge
            FROM test_db.airplanecrawl
            WHERE date = '{selected_date}'
            ORDER BY charge ASC
            LIMIT 10;
            '''
    else:
    # 데이터베이스에서 선택된 날짜의 데이터를 가져오는 코드
        sql = f'''
            SELECT date, day, name, airport, leavetime, reachtime, seat,charge
            FROM test_db.airplanecrawl
            WHERE date = '2023-07-01'
            ORDER BY charge ASC
            LIMIT 10;
        
    '''
    air_data = clinet_bigquery(sql)
    air_list = air_data.to_dict(orient='records')
    hotel_list = hotel_data.to_dict(orient='records')
    car_list = car_data.to_dict(orient='records')
    
    if request.method == 'POST':
        # air_data를 JSON 형식으로 변환하여 반환
        return jsonify(air_list=air_list, hotel_list=hotel_list, car_list=car_list,num=num)
    else:
        # HTML 템플릿 렌더링 및 반환
        return render_template('filght.html', 
                               air_list=air_list,
                               hotel_list=hotel_list,
                               car_list=car_list
                               ,num=num)
    

@app.route('/filghtDate', methods=['GET','POST'])
def filghtDate(selectedDate=None,statusselect2=None ):
    if request.method == 'POST':
        pass
    else:
        selectedDate = request.args.get('selectedDate')
        statusselect2 = request.args.get('statusselect2')
        sql = f'''
            SELECT date, day, name, airport, leavetime, reachtime, seat,charge
            FROM test_db.airplanecrawl
            WHERE date = '{selectedDate}' AND airport = '{statusselect2}'
            ORDER BY charge ASC
            LIMIT 10
            '''
        air_data = clinet_bigquery(sql)
        air_list = air_data.to_dict(orient='records')
        return render_template('filght.html', air_list=air_list)
