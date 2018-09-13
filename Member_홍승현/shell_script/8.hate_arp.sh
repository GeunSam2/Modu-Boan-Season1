8. hate_arp.sh
매 3분마다 내 컴퓨터에서 arp스푸핑이 일어나고 있는지에 대한 검사를 하는 감시프로그램과,
감시프로그램을 종료할때 사용할 종료프로그램을 만드시오.
- arp스푸핑이 감지되면, arp스푸핑공격을 수행중인 공격자의 ip를 찾아내어 이용자의 화면에 경고메시지를
출력하도록 하세요.
- 종료프로그램은 오직 arp스푸핑 감시프로그램을 종료하는 용도로만 사용됩니다.

#!/bin/bash

iptable=(
)
mactable=(
)

count=0
exist=0
for i in $(arp | grep ':')
do
	if [ `expr $count % 5` = 0 ];then
		iptable[exist]=$i
	elif [ `expr $count % 5` = 2 ];then
		mactable[exist]=$i
		#echo -e "IP:\t${iptable[exist]} \tMAC: ${mactable[exist]}"
		(( exist++ ))
	fi
	(( count++ ))
done

while [ 1 ]
do
comp_iptable=(
)
comp_mactable=(
)
	count=0
	exist=0
	for i in $(arp | grep ':')
	do
		if [ `expr $count % 5` = 0 ];then
			comp_iptable[exist]=$i
		elif [ `expr $count % 5` = 2 ];then
			comp_mactable[exist]=$i
			echo -e " IP:\t${iptable[exist]}\t MAC: ${mactable[exist]}"
			echo -e "CIP:\t${comp_iptable[exist]}\tCMAC: ${comp_mactable[exist]}"
			(( exist++ ))
		fi
		(( count++ ))
	done

	j=0
	while [ $j != $exist ]
	do
		i=0
		while [ $i != $exist ]
		do
			if [ ${comp_iptable[j]} = ${iptable[i]} ];then
				if [ ${comp_mactable[j]} = ${mactable[i]} ];then
					echo -e "***\t"${comp_iptable[j]}"\t"PASS
				else
					echo -e "***\t"${comp_iptable[j]}"\t"ARPSPOOFING"\t"ATTACKER IP: ${comp_iptable[j]}
				break;
				fi
			fi
		(( i++ ))
		done
	(( j++ ))
	done
	
	echo ""
	sleep 3
done

방식: 처음 실행시키면 arp테이블을 조회해서 IP와 MAC주소를 맵핑해서 보관하고 그 이후에 3초마다 arp테이블을 조회하고
	등록된 IP에 맵핑된 MAC주소가 바뀌었으면 탐지했다고 나옵니다. 뭔가 허술한 것 같은 느낌..
	실험은 못 해봤습니다..ㅎㅎㅎ
	
종료프로그램

#!/bin/bash

killall -9 hate_arp.sh
