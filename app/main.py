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
            SELECT date, CAST(AVG(charge) AS INT64) AS avgcharge, MIN(charge) AS mincharge, MAX(charge) AS maxcharge
            FROM test_db.airplanecrawl
            GROUP BY date
            ORDER BY date
            LIMIT 500;
        '''
        data_list = clinet_bigquery(sql)
        json_data = data_list.to_json(orient='records')

        return jsonify(json_data)

air_data = clinet_bigquery('''
                            SELECT date, day, name, airport, leavetime, reachtime, seat,charge
                            FROM test_db.airplanecrawl
                            WHERE date = '2023-07-01'
                            ORDER BY charge ASC
                            LIMIT 10;
                            ''')
hotel_data = clinet_bigquery('''SELECT * FROM test_db.hotelcrawl
                                where rating != '평점없음' and star is not null
                                order by star desc, price asc
                                LIMIT 10;''') 
car_data = clinet_bigquery('''SELECT  carname, oiltype, seater, avg_year,
                            CAST(AVG(CAST(regular_price AS INT)) AS INT) AS avg_regular_price,
                            CAST(AVG(CAST(discounted_price AS INT)) AS INT) AS avg_discounted_price
                            FROM `fightproject.test_db.car`
                            WHERE regular_price != '마감' AND discounted_price != '마감'
                            GROUP BY carname, oiltype, seater, avg_year
                            ORDER BY avg_discounted_price, avg_regular_price
                            LIMIT 10;''') 

@app.route('/filght', methods=['GET','POST'])
def get_flight():
    air_list = air_data.to_dict(orient='records')
    hotel_list = hotel_data.to_dict(orient='records')
    car_list = car_data.to_dict(orient='records')

    if request.method=='POST':
        return jsonify(air_list=air_list, hotel_list=hotel_list, car_list=car_list)
    else:
        return render_template('filght.html', air_list=air_list, hotel_list=hotel_list, car_list=car_list)



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
        hotel_list = hotel_data.to_dict(orient='records')
        car_list = car_data.to_dict(orient='records')
        return render_template('filght.html', air_list=air_list, hotel_list=hotel_list, car_list=car_list)

@app.route('/dashboard1') 
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

if __name__ == '__main__':
    app.run(debug=True)  