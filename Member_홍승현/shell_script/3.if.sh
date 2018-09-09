3번. if.sh
현재 내가 있는 디렉토리의 위치를 확인한 뒤,
내가 지금 있는 디렉토리가 '자기이름폴더'라면 화면에 'Your home!'을 출력하고,
그렇지 않다면, 'Where am i?'를 출력한 뒤, '자기이름 폴더'로 이동합니다.
이동 한 뒤에는 현재 디렉토리의 파일 목록들을 '-al'옵션을 붙여서 표시해 줍니다.

#!/bin/bash

home=($pwd)

if [ "$home" =  "/root/moduboan/hong_seung_hyun" ]; then
	echo "Your home!"
else
	echo "Where am I?"
	cd /root/moduboan/hong_seung_hyun
	ls -al
fi
