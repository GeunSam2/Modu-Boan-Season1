#!/bin/bash

a=$(pwd)

if [ $a = /root/moduboan/Kang_Min_Suk ];then
	echo YOUR HOME!!
else
	echo Where am i?
	cd /root/moduboan/Kang_Min_Suk
	ls -al
fi
