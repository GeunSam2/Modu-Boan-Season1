#!/bin/bash

#echo 1:$1 2:$2 3:$3 4:$0 5:$#
Dir1=/root/moduboan/yeom_geun_cheol
if [ $# -ne 2 ] || [[ $1 =~ [^123] ]] || [[ $2 =~ 'show|store' ]]; then
	echo Usage : $0 [1-3] [show/store]
	exit 1
fi

case $1 in
	1) ifconfig | awk '/broadcast/{print "ipv4 : "$2}';;
	2) netstat -nr;;
	3) arp;;
esac > $Dir1/level7.tmp

if [ $2 == 'show' ]; then
	cat $Dir1/level7.tmp
	rm $Dir1/level7.tmp
fi

