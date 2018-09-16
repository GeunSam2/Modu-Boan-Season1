8. hate_arp.sh
매 3분마다 내 컴퓨터에서 arp스푸핑이 일어나고 있는지에 대한 검사를 하는 감시프로그램과,
감시프로그램을 종료할때 사용할 종료프로그램을 만드시오.
- arp스푸핑이 감지되면, arp스푸핑공격을 수행중인 공격자의 ip를 찾아내어 이용자의 화면에 경고메시지를
출력하도록 하세요.
- 종료프로그램은 오직 arp스푸핑 감시프로그램을 종료하는 용도로만 사용됩니다.

#!/bin/bash

first_table=()

exist=0
count=0
echo "STATIC ARP TABLE -------------------------------------"
for i in $(arp -n | grep ':')
do
	if [ `expr $count % 5` = 0 ];then
		first_table[exist]=$i
		#echo ${first_table[exist]}
	elif [ `expr $count % 5` = 2 ];then
		first_table[exist]=${first_table[exist]}" "$i
		echo ${first_table[exist]}
		(( exist++ ))
	fi
	(( count++ ))
done
echo "STATIC ARP TABLE -------------------------------------"

echo -e "\nwrite current MAC address in hi.text -----------------"
for ((i=0;i<$exist;i++))
do
	echo ${first_table[$i]} | awk '{print $2}' >> hi.text
done
`cat ./hi.text | uniq -d > hi.text`

chmod +x hi.text
echo -e "\ncompare STATIC ARP TABLE and current arp table -------"

total_flag=0
while read line
do
	echo "compare to" $line
	flag=0
		for ((j=0;j<$exist;j++))
		do
			#echo $line
			comp=`echo ${first_table[j]} | awk '{print $2}'`
			#echo $comp
			if [ "$line" = "$comp" ]; then
				echo attacker_ip: ${first_table[j]} | awk '{print $1}'
				total_flag=1
				flag=1
			fi
		done
	if [ $flag = 0 ];then
		echo PASS
	fi
done < hi.text

if [ $total_flag = 0 ];then
	echo -e "\n---------------------------------------------YOUR SAFE\n"
fi

rm hi.text
echo "remove hi.text ---------------------------------------"
