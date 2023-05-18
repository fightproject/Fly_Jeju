from flask import Flask, render_template,request
from bigquery import clinet_bigquery


app = Flask(__name__, static_url_path="/static")

@app.route('/')
def calendar():
    return render_template('main.html')

@app.route('/filght',methods=['GET','POST'])
def flight():
    # 데이터불러오기
    data = clinet_bigquery('app/config/*.json', 'select * from test_db.airplane limit 500') 

    # 시간을 2030 -> 20:30 으로 표현하기 위한 코드 
    dep_hour= data['dep_time'].apply(lambda x: str(x)[:-2])
    dep_minute = data['dep_time'].apply(lambda x: str(x)[-2:])
    arr_hour=data['arr_time'].apply(lambda x: str(x)[:-2])
    arr_minute = data['arr_time'].apply(lambda x: str(x)[-2:])

    # 옵션에서 선택하면 가격에 맞는 값만 보여주도록함.
    if request.method == 'POST':
        selected_option = request.form.get('status-select')
        if selected_option == '1':  # 0~50k 선택한 경우
            filtered_data = data[data['price'] <= 50000]
        elif selected_option == '2':  # 50~100k 선택한 경우
            filtered_data = data[(data['price'] > 50000) & (data['price'] <= 100000)]
        elif selected_option == '3':  # 100~150k 선택한 경우
            filtered_data = data[(data['price'] > 100000) & (data['price'] <= 150000)]
        elif selected_option == '4':  # 150~200k 선택한 경우
            filtered_data = data[(data['price'] > 150000) & (data['price'] <= 200000)]
        elif selected_option == '5':  # 200k~ 선택한 경우
            filtered_data = data[data['price'] > 200000]
        else:
            filtered_data = data  # 선택하지 않은 경우, 모든 데이터를 출력

        return render_template('filght.html',
                               data=filtered_data,
                               dep_hour=dep_hour,
                               dep_minute=dep_minute,
                               arr_minute=arr_minute,
                               arr_hour=arr_hour)

    # 실행시 데이터를 그냥 불러옴.
    return render_template('filght.html',
                           data = data, 
                           dep_hour=dep_hour,     
                           dep_minute=dep_minute, 
                           arr_minute = arr_minute,   
                           arr_hour = arr_hour)


@app.route('/dashboard1') 
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

if __name__ == '__main__':
    app.run(port='5000', debug=True)  