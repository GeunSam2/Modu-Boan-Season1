import requests
from bs4 import BeautifulSoup as bs


# 플레이어 이름을 입력
a=input('ID 입력 : ')

url='http://fow.kr/find/'+str(a)

re=requests.get(url)


bt=bs(re.text,'html5lib')


# 변수 'c' 에 최근 전적 내용을 str 로 저장
c=bt.find_all("div",style="top:7px; left:155px; line-height:14px; position:absolute;")[0].text[6:]
# split 함수를 통해 공백을 기준으로 'c' 에 리스트 형식으로 저장을 해서 내가 뽑고 싶은 내용을 출력
print("플레이어 정보 : ",c)
print("")

# 최근 전적을 포함하고 있는 css 내용을 문자열 슬라이싱을 통해 출력
d=bt.find_all("span",style="font-size:24px; font-weight: 900; color:#000;")[0].text[4:7]
print("최근 전적 : ",d.strip(),bt.find_all("span",style="font-size:24px; font-weight: 900; color:#292;")[0].text[4:7],bt.find_all("span",style="font-size:24px; font-weight: 900; color:#B00;")[0].text[4:7])

print("")


print("공백없이 입력하세요!!!!!!!!!!!")
print("한국어만 입력 가능!!")
print("")
b=input("챔피언 : ")


for i in range(7):
    # select 함수를 이용해서 내가 뽑고 싶은 테이블을 변수 'e' 에 저장
    # 모스트 챔피언의 데이터를 0~6 번 째 까지 'e' 에 저장
    e=bt.select(".tablesorter tr[style=font-size:12px;]")[i]

    # 변수 'f' 에 필요 없는 문자를 'replace' 함수로 변환
    f=[e.text.replace("\n",",").replace(" ","").replace(","," ")][0]

    # 모스트 7 안에 드는 챔프를 할경우 정상적으로 실행
    # 승률에 따라 게임을 플레이 할지 닷지를 할지 조언을 날려줌
    if str(b) in f:
        print("승률 : ",f.split()[2])
        if 50 <= float(f.split()[2].replace("%","")) <70:
            print("승률 봐줄만함 닷지 ㄴㄴ\n")
        if 70 <= float(f.split()[2].replace("%","")) < 100:
            print("승률 개높음 버스 받아")
        if  50 > float(f.split()[2].replace("%","")) > 40:
            print("너가 캐리할자신 없으면 닷지 추천!")
        if float(f.split()[2].replace("%","")) < 40:
            print("그냥 무조건 닷지!!!")

print("결과 값이 안나올 경우 모스트 챔피언이 아니므로 플레이시 주의 요망 !")
        

