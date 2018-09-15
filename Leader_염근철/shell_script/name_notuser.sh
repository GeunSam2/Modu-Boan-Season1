#!/bin/bash
Dir1=/root/moduboan/yeom_geun_cheol
for i in `cat $Dir1/notuser.txt`
do
	echo $i can\'t be login
done > $Dir1/name_notuser.txt
