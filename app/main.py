from flask import Flask, render_template,request
from bigquery import clinet_bigquery


app = Flask(__name__, static_url_path="/static")

total_amount = 0

@app.route('/')
def calendar():
    return render_template('main.html')

@app.route('/filght',methods=['GET','POST'])
def flight():
    global total_amount
    # 호텔데이터불러오기(기본)
    hotel_data = clinet_bigquery('app/config/*.json', 
                                 '''SELECT * FROM jeongsu_test.hotel_crawling_data
                                    WHERE hotel_star != 0 OR hotel_rating != 0 OR hotel_price != 0
                                    ORDER BY hotel_rating DESC, hotel_price ASC
                                    LIMIT 100;''',1) 
    
    # 항공권 데이터 불러오기(기본)
    air_data = clinet_bigquery('app/config/*.json', 
                                 '''SELECT * FROM test_db.airplanecrawl
                                    ORDER BY charge ASC, date ASC, leavetime ASC
                                    LIMIT 100;''',0) 


    def option_func(selected_option,data,columns):       
        if selected_option == '1':  # 0~50k 선택한 경우 
            filtered_data = data[(data[columns] < 50000)]
        elif selected_option == '2':  # 50~100k 선택한 경우
            filtered_data = data[(data[columns] > 50000) & (data[columns] <= 100000)]
        elif selected_option == '3':  # 100~150k 선택한 경우
            filtered_data = data[(data[columns] > 100000) & (data[columns] <= 150000)]
        elif selected_option == '4':  # 150~200k 선택한 경우
            filtered_data = data[(data[columns] > 150000) & (data[columns] <= 200000)]
        elif selected_option == '5':  # 200k~ 선택한 경우
            filtered_data = data[data[columns] > 200000]
        else:
            filtered_data = data  # 선택하지 않은 경우, 모든 데이터를 출력

        return filtered_data

    if request.method == 'POST':
        # 항공권에서 옵션 선택했을 때

        selected_air = request.form.getlist('customCheck1')
        selected_hotels = request.form.getlist('customCheck2')
        total_amount = int(sum(float(air_data[int(index)]['charge']) for index in selected_air) + sum(float(hotel_data[int(index)]['hotel_price']) for index in selected_hotels))

        if 'status-select' in request.form:
            selected_option1 = request.form.get('status-select')
            filtered_data1 = option_func(selected_option1, air_data, 'charge')
            return render_template('filght.html', total_amount=total_amount, hotel_data=hotel_data, air_data=filtered_data1)

        # 호텔에서 옵션 선택했을 때
        elif 'status-select3' in request.form:
            selected_option3 = request.form.get('status-select3')
            filtered_data3 = option_func(selected_option3, hotel_data, 'hotel_price')
            return render_template('filght.html', total_amount=total_amount, hotel_data=filtered_data3, air_data=air_data)


    # 실행 시 데이터를 그냥 불러옴.
    return render_template('filght.html',
                           hotel_data=hotel_data,
                           air_data=air_data,
                           total_amount=total_amount)

@app.route('/dashboard1') 
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

if __name__ == '__main__':
    app.run(debug=True)  