7번. ifconfig.sh
네트워크 정보를 보거나, 수정하는 툴을 만듭니다.
argument.sh 는 두개의 인자를 받아서 실행되어야 합니다.
ex) ./argument.sh [인자1] [인자2]
- 입력받은 인자가 2개가 되지 않으면, 오류 메시지를 출력하고 실행을 종료합니다.
- 인자1 에는 1~3의 숫자를 입력받고, 해당 범위를 벗어나면 오류 메시지를 출력하고 실행을 종료합니다.
- 인자2 에는 show / store 두개의 문자열만 입력받을 수 있습니다. 이외의 문자열을 입력받으면 오류 메시지를 출력하고 실행을 종료합니다.

- 인자1 에 1~3을 입력받으면, 각각 다르게 동작합니다.
    입력받은 문자가 '1'일때 : 현재 자신의 ip정보 출력(ipv4주소만 출력)
    입력받은 문자가 '2'일때 : 현재 자신의 라우팅 테이블 출력
    입력받은 문자가 '3'일때 : 현재 자신의 arp캐시테이블 출력

- 인자2 에 show/store 문자열을 입력받으면 각각 다르게 동작합니다.
    입력받은 문자가 'show'일때 : 인자1에 대한 출력결과를 그대로 화면에 보여줍니다.
    입력받은 문자가 'store'일때 : '자기이름폴더' 아래에 level7.tmp 파일로 출력결과를 저장합니다.(화면에는 출력하지 않습니다.)

#!/bin/bash

if [ $1 ] && [ $2 ];then
	if [ $1 = 1 ] || [ $1 = 2 ] || [ $1 = 3 ];then
		if [ $2 = "show" ];then
			if [ $1 = 1 ];then
				ifconfig | grep -m 1 inet | cut -c 14-24	
			elif [ $1 = 2 ];then
				route
			else
				arp -n
			fi
		elif [ $2 = "store" ];then
			if [ $1 = 1 ];then
				ifconfig | grep -m 1 inet | cut -c 14-24 >> /root/moduboan/hong_seung_hyun/level7.tmp
			elif [ $1 = 2 ];then
				route >> /root/moduboan/hong_seung_hyun/level7.tmp
			else
				arp -n >> /root/moduboan/hong_seung_hyun/level7.tmp
			fi
		else
			echo "second argument has to 'show'or'store'"
			exit
		fi
	else	
		echo "first argument has to '1'or'2'or'3'"
		exit
	fi
else
	echo "input 2 arguments"
	exit
fi
