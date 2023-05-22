from flask import Flask, render_template, jsonify
from bigquery import *
import json

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def calendar():

    sql = '''
    select date, day, price
    from test_db.airplane 
    limit 10
    '''
    data_list = bigqueryCall(sql)
    print(data_list) #데이터 프레임

    # 데이터 프레임을 JSON으로 변환
    json_data = data_list.to_json(orient='records')
    parsed_data = json.loads(json_data)
    
    print("데이터타입 : ", type(parsed_data))
    for airplane in parsed_data:
        print(airplane)
    print("===================================== airplane 끝 =====================================")

    return render_template('main.html',data_list=data_list, json_data=json_data)

@app.route('/filght')
def filght():
    return render_template('filght.html')


@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')


@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')


if __name__ == '__main__':
    app.run(port='5000', debug=True)
