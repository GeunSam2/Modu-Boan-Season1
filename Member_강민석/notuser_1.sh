#!/bin/bash

count=0
while read line
do
	a=`echo $line | cut -d ':' -f7`
	if [ $a = /usr/sbin/nologin ] || [ $a = /bin/false ] || [ $a = /sbin/nologin ] || [ $a = /bin/sync ] || [ $a = /bin/sh ]; then
		count=$(($count+1))
	fi
done < /etc/passwd
echo $count


