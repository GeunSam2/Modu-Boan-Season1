5번. name_notuser.sh
/etc/passwd 파일에서 로그인 쉘이 없는 사용자들의 이름만 추출하여
이름뒤에 'can't be login' 이라는 문장을 붙여서
'자기이름폴더' 아래에 name_notuser.txt 로 저장하는 툴을 만들어라.
ex)
------ name_notuser.txt ------
sshd can't be login
gluster can't be login

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
