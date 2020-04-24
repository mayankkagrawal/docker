#!/usr/bin/python3.6

print('content-type: text/html')
print()
import os

os.system("echo -e -n '[dvd1] \nbaseurl=file:///dvd2/AppStream \ngpgcheck=0 \n[dvd2] \nbaseurl=file:///dvd2/BaseOS \ngpgcheck=0'>/etc/yum.repos.d/lw.repo")

