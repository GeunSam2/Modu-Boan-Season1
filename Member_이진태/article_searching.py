import requests
from bs4 import BeautifulSoup as bs

url = 'https://sports.news.naver.com/wfootball/news/index.nhn?type=latest'
respone = requests.get(url)
respone.encoding="UTF-8"

soup=bs(respone.text,"html5lib")

count = 0
li=1

article_list = soup.find("div",class_="aside_rank_news").find_all("li")
print("------전체 기사-----")
for i in article_list:
	print(li,"..."+i.string)
	li+=1

print("--------------------------------------------")
print("키워드를 입력하세요 : ",end='')
keyword=input()
print("------------------검색결과---------------------")

for i in article_list:
	if keyword in i.string:
		count+=1
		print(i.string)
if count==0:
	print("일치하는 결과가 없습니다.")
print("============================================")
print(keyword+"(이)가 언급된 기사는",count,"개 입니다.")
