#!/bin/bash
Tmp1=/tmp/level8.tmp
Swc=1
arp -n | grep -v Address | awk '{print $1";"$3}' > ${Tmp1}${Swc}
while true 
do
	sleep 3
	Swc=`expr $Swc \* -1`
	arp -n | grep -v Address | awk '{print $1";"$3}'>${Tmp1}${Swc}
	count1=`awk -F\; '{print $2}' ${Tmp1}${Swc} | sort | uniq -d`
	if [ $count1 ]; then
		wall "You Are UnderAttack!! (code:ARP)"
		if [ $(grep $count1 -c ${Tmp1}`expr $Swc \* -1`) -ne 1 ]; then
			wall "Can't find Attacker. But UnderAttack!"
		else
			hacker=$(grep $count1 ${Tmp1}`expr $Swc \* -1` | awk -F\; '{print $1}')
			echo hacker is $hacker
		fi
	fi
done
