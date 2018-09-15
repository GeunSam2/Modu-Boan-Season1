#!/bin/bash

Dir1=/root/moduboan/yeom_geun_cheol
if [ `pwd` == $Dir1 ]; then
	echo 'Your home!'
else
	echo 'Where am i?'
	cd $Dir1
fi

ls -al

