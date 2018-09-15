#!/bin/bash

Dir1=/root/moduboan/yeom_geun_cheol
awk -F: '/nologin|false/{print $1}' /etc/passwd > $Dir1/notuser.txt
Count=`wc -l $Dir1/notuser.txt | awk '{print $1}'`
echo 로그인 못하는 찌질이들 : $Count명
