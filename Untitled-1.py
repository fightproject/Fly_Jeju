import datetime

def dayConvert(date):
    #20230519
    day = datetime.date(date//10000, date%10000//100, date%100).weekday()
    dayDate = '월화수목금토일'
    return dayDate[day]

print(dayConvert(20230519))