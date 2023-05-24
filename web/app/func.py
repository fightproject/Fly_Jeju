from bigquery import clinet_bigquery

def air_filter_test(filepath, value):
    value = int(value)
    if value <= 20:
        sql =f'''SELECT *
                FROM `fightproject.test_db.airplanecrawl`
                WHERE charge <= {value}0000;'''
    elif value > 20:
        sql =f'''SELECT *
                FROM `fightproject.test_db.airplanecrawl`
                WHERE charge > {value}0000;'''
        
    return clinet_bigquery(filepath, sql, 0)


# 가격 범위 설정에 따른 결과값을 보여주기위한 함수.
def air_price_option_func(selected_option,data,columns):       
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

# 출발지에 따른 결과값을 보여주기위한 함수
def air_port_option_func(selected_option,data,columns):       
    if selected_option == '1':  
        filtered_data = data[(data[columns]=='GMP')]
    elif selected_option == '2': 
        filtered_data = data[(data[columns]=='CJU')]
    else:
        filtered_data = data  # 선택하지 않은 경우, 모든 데이터를 출력
    return filtered_data

# 호텔 주소에 따른 결과값을 보여주기위한 함수
def hotel_option_func(selected_option,data,columns):       
    if selected_option == '1':   
        filtered_data = data[(data[columns]=='제주')]
    elif selected_option == '2': 
        filtered_data = data[(data[columns]=='서귀포')]
    else:
        filtered_data = data  # 선택하지 않은 경우, 모든 데이터를 출력
    return filtered_data

# 날짜에 따른 결과값을 보여주기위한 함수
def date_option_func(selected_option,data,columns):       
    filtered_data = []
    for item in data:
        if item[columns] == selected_option:
            filtered_data.append(item)
    return filtered_data