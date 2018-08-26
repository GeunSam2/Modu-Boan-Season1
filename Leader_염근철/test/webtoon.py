from selenium import webdriver
from bs4 import BeautifulSoup as bus

driver = webdriver.Chrome('D:\모의해킹침해대응15기\정리\chromedriver.exe')
#driver.implicitly_wait(3)
driver.get('http://webtoon.daum.net/ranking')
html = driver.page_source
soup = bus(html, 'html5lib')
#rank_list = soup.find_all('li',class_='item_rank')
rank_list2 = soup.select('li > a > span.info_append > strong')


for i,j in enumerate(rank_list2):
    print (str(i+1)+"위 : "+j.text)


