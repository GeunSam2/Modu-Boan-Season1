6번. chmod.sh
현재폴더 아래에 있는 파일들을 검사하여,
쉘스크립트 형식인 파일 중, 실행권한이 없는 파일이 총 몇개인지 표시하고,
그 파일들에 실행권한을 부여하는 툴을 만들어라.

#!/bin/bash

count=0

for i in *.sh
do
	if [ -x "$i" ];then
		a="a" #cause error
	else
		chmod +x $i
		(( count++ ))
	fi
done
echo $count
