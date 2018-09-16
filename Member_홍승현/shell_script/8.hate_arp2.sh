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

방식: 처음 실행할 때 arp table의 ip와 mac주소를 저장하고 그 mac주소들 중 중복된 값이 있다면 그 mac주소를 hi.text에 저장한다.
	이 저장된 mac주소와 처음 저장한 table을 조회하여 맵핑 된 ip를 출력한다. crontab을 사용하기 때문에
	while문을 뺏고 hi.text도 매 번 삭제해준다.

의문: grep이나 awk를 사용하여 for문을 돌 때 공백을 기준으로 하여서 원하는 정보를 뽑아 낼 수가 없는데 이 때 공백이 기준이 되지않고
	한줄이 기준이 될 수 있나?
	ex) arp의 결과가
		Address		 HWtype 	HWaddress
		192.186.0.1			54:8e:0a:00:2b:a1
	이라면 for i in $(arp)를 하엿을 때 i가 Address > HWtype > HWaddress > 192.186.0.1 > 54:8e:0a:00:2b:a1 순으로 변하는데
	이 때 i가 Address HWtype HWaddress > 192.168.0.1	54:8e:0a:00:2b:a1 이렇게 저장이 된다면
	`expr $count %5 = 0`같은건 안 해도 된다.
	
근철씨 코드를 보고 나니 조잡하단 걸 느꼇습니다ㅋㅋㅋ 저도 배열 사용 안 하고 처음 맵핑을 파일로 출력해도 될 것 같습니다
