3번. if.sh
현재 내가 있는 디렉토리의 위치를 확인한 뒤,
내가 지금 있는 디렉토리가 '자기이름폴더'라면 화면에 'Your home!'을 출력하고,
그렇지 않다면, 'Where am i?'를 출력한 뒤, '자기이름 폴더'로 이동합니다.
이동 한 뒤에는 현재 디렉토리의 파일 목록들을 '-al'옵션을 붙여서 표시해 줍니다.

#!/bin/bash

while read line
do
	shell=`echo $line | cut -d':' -f7`
	if [ $shell = "/usr/sbin/nologin" ] || [ $shell = "/bin/false" ] || [ $shell = "/bin/sync" ] || [ $shell = "/sbin/nologin" ];then
		a="can't be login"
		b=`echo $line | cut -d':' -f1`
		echo $b $a >> /root/moduboan/hong_seung_hyun/name_notuser.txt
	fi
done < /etc/passwd
