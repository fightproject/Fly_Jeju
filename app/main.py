from flask import Flask, render_template, request, jsonify
from bigquery import clinet_bigquery
import func
import json



app = Flask(__name__, static_url_path="/static")

total_amount = 0

@app.route('/')
def calendar():
    return render_template('main.html')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        data = request.form.get('data')
        return "POST 요청을 받았습니다"
    else:
        sql = '''
            SELECT date, charge
            FROM test_db.airplanecrawl 
            LIMIT 50
        '''
        data_list = clinet_bigquery('./app/config/*.json',sql,0)
        json_data = data_list.to_json(orient='records')
        print(data_list)

        return jsonify(json_data)

@app.route('/filght',methods=['GET','POST'])
def flight():
    global total_amount
    # 호텔데이터불러오기(기본)
    hotel_data = clinet_bigquery('./app/config/*.json', 
                                 '''SELECT * FROM test_db.hotelcrawl
                                    where rating != '평점없음' and star is not null
                                    LIMIT 500;''',0) 
    # 항공권 데이터 불러오기(기본)
    air_data = clinet_bigquery('./app/config/*.json', 
                                 '''SELECT * FROM test_db.airplanecrawl
                                    LIMIT 300;''',0) 
    
    # 렌터카 데이터 불러오기(기본)
    car_data = clinet_bigquery('./app/config/*.json', 
                                 '''SELECT  carname, oiltype, seater, avg_year,
                                    CAST(AVG(CAST(regular_price AS INT)) AS INT) AS avg_regular_price,
                                    CAST(AVG(CAST(discounted_price AS INT)) AS INT) AS avg_discounted_price
                                    FROM `fightproject.test_db.car`
                                    WHERE regular_price != '마감' AND discounted_price != '마감'
                                    GROUP BY carname, oiltype, seater, avg_year
                                    ORDER BY avg_discounted_price, avg_regular_price;''',0) 

    # 웹페이지에서 요청이 들어왔을때
    if request.method == 'POST':
        # 항공권과 호텔, 렌터카에 대한 총합 보여주기위함.
        selected_air = request.form.getlist('customCheck1')
        selected_hotels = request.form.getlist('customCheck2')
        selected_car = request.form.getlist('customCheck3')
        total_amount = sum(float(air_data[int(index)]['charge']) for index in selected_air) + \
                    sum(float(hotel_data[int(index)]['price']) for index in selected_hotels) + \
                    sum(float(car_data[int(index)]['avg_discounted_price']) for index in selected_car)
                            

        # 항공권에서 가격범위옵션 선택했을 때
        if 'status-select' in request.form:
            selected_option1 = request.form.get('status-select')
            filtered_data1 = func.air_price_option_func(selected_option1, air_data, 'charge')
            return render_template('filght.html', total_amount=total_amount, hotel_data=hotel_data, air_data=filtered_data1,car_data=car_data)

        # 항공권 출발지 옵션 선택했을때
        elif 'status-select2' in request.form:
            selected_option2 = request.form.get('status-select2')
            filtered_data2 = func.air_port_option_func(selected_option2, air_data, 'airport')
            return render_template('filght.html', total_amount=total_amount, hotel_data=hotel_data, air_data=filtered_data2,car_data=car_data)
        
        # 호텔에서 가격범위옵션 선택했을 때
        elif 'status-select3' in request.form:
            selected_option3 = request.form.get('status-select3')
            filtered_data3 = func.option_func(selected_option3, hotel_data, 'price')
            return render_template('filght.html', total_amount=total_amount, hotel_data=filtered_data3, air_data=air_data,car_data=car_data)
        
        # 호텔 주소옵션 선택했을때
        elif 'status-select4' in request.form:
            selected_option4 = request.form.get('status-select4')
            filtered_data4 = func.hotel_option_func(selected_option4, hotel_data, 'address')
            return render_template('filght.html', total_amount=total_amount, hotel_data=hotel_data, air_data=filtered_data4,car_data=car_data)

        # 날짜 옵션 선택했을떄
        elif 'date-select' in request.form:
            selected_option5 = request.form.get('date-select')
            filtered_data5 = func.date_option_func(selected_option5, air_data, 'date')
            return render_template('filght.html', total_amount=total_amount, hotel_data=hotel_data, air_data=filtered_data5,car_data=car_data)
        

    # 웹페이지 열었을때 보여지는 데이터.
    return render_template('filght.html',
                           hotel_data=hotel_data,
                           air_data=air_data,
                           total_amount=total_amount,
                           car_data=car_data)

@app.route('/dashboard1') 
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

if __name__ == '__main__':
    app.run(debug=True)  