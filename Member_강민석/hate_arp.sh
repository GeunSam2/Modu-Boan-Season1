#!/bin/bash

a=$(arp -n | awk '/192.168.147.1 /{print $3}')
while [ 1 ]
do
	echo watching your arp !!!!!
	for i in $(arp -n | awk '/192.168/{print $1}')
	do
		for j in $(arp -n | awk '/192.168/{print $3}')
		do
			echo IP : $i MAC : $j
			echo --------------------------------------------------
			if [ $j == $a ]; then
				echo ************** Find Out ******************
				echo Attacker IP : $i
			fi	
		done	
	done

	sleep 180
done


