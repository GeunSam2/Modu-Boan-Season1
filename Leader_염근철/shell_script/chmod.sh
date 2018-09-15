#!/bin/bash

Count=0
for i in `ls`
do
	Type1=`file $i | grep -c shell`
	if [ $Type1 -eq 1 ]; then
		Type2=`ls $i -l | awk '{print $1}' | grep -c x`
		if [ $Type2 -eq 0 ]; then
			chmod u+x $i
			Count=`expr $Count + 1`
		fi
	fi
done

echo 실행권한 없는 파일 : $Count개
echo 변환완료
