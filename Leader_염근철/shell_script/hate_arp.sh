#!/bin/bash
Tmp1=/tmp/level8.tmp
Swc=1
arp -n | grep -v Address | awk '{print $1";"$3}' > ${Tmp1}${Swc}
while true 
do
	sleep 3
	Swc=`expr $Swc \* -1`   //스위치 변수입니다. 1회전 할 때마다 1, -1로 변화합니다.
	arp -n | grep -v Address | awk '{print $1";"$3}'>${Tmp1}${Swc}   //스위치 변수를 활용하여 두개의 Temp파일에 번갈아 저장합니다.
	hacker_mac=`awk -F\; '{print $2}' ${Tmp1}${Swc} | sort | uniq -d` //공격자의 맥주소를 검출합니다.
	if [ $hacker_mac ]; then
		wall "You Are UnderAttack!! (code:ARP)"
		if [ $(grep $hacker_mac -c ${Tmp1}`expr $Swc \* -1`) -ne 1 ]; then //이전 Temp에 공격자가 없었거나, 이미 공격당하고 있는 상황일 경우 입니다.
			wall "Can't find Attacker. But UnderAttack!"
		else        //공격자를 특정할 수 있는 상황입니다.
			hacker=$(grep $hacker_mac ${Tmp1}`expr $Swc \* -1` | awk -F\; '{print $1}')
			echo hacker is $hacker
		fi
	fi
done
