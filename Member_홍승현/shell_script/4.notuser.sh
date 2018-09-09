4번. notuser.sh
/etc/passwd 파일에서 로그인 쉘이 없는 사용자들 목록을 불러와서,
'자기이름폴더' 아래에 notuser.txt 파일 안에 저장한 뒤
위조건에 해당하는 사용자 수가 총 몇명인지 표시하는 툴을 만들어라.

#!/bin/bash

count=0
while read line
do
	shell=`echo $line | cut -d':' -f7`
	if [ $shell = "/usr/sbin/nologin" ] || [ $shell = "/bin/false" ] || [ $shell = "/bin/sync" ] || [ $shell = "/sbin/nologin" ];then
		(( count++ ))
	fi
done < /etc/passwd
echo $count
