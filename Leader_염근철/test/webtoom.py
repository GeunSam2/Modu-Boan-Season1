import requests
from bs4 import BeautifulSoup
import re

bfs = BeautifulSoup

URL = "http://webtoon.daum.net/ranking"

s = requests.Session()
req = requests.Request('get',URL)
pre = s.prepare_request(req)
reqs = s.send(pre)

bu1 = bfs(reqs.text,'html5lib')
print (bu1.find_all('strong class="tit_wt"'))