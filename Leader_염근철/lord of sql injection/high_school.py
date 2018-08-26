import requests
from bs4 import BeautifulSoup

bfs = BeautifulSoup

URL = "https://gds.hs.kr/lib/loginpost.php"
#cookie = {}

s = requests.Session()

data = {
    "mem_id":"123",
    "passwd":"123",
    "x":"0",
    "XQUEDATA":"IjtzOjA6IiI7czo5OiJ0YXJnZXRVcmwiO3M6MTQ6Ii9tYWluL21haW4ucGhwIjt9YTozOntzOjExOiJxdWVyeUVuY29kZSI7czowOiIiO3M6MTE6InRhcmdldEZyYW1l",
    "y":"0"
}

req  =requests.Request('post',URL,data=data)
prepare = s.prepare_request(req)
req1 = s.send(prepare)
req1.encoding = None
bu1 = bfs(re1.text,'html5lib')
print (bfs.prettify(bu1))
