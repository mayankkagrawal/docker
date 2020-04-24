#!/usr/bin/python3.6

print('content-type: text/html')
print()

#import cgi 
import os
import subprocess
#form=cgi.FieldStorage()
#user=form.getvalue('user')

x=subprocess.getstatusoutput('sudo yum install httpd -y')
if x[0]==0:
    os.system('sudo /usr/sbin/httpd')
    os.system("echo -e -n ' \nrm -rf /var/run/httpd/* \n/usr/sbin/httpd'>>/root/.bashrc ")
    print("succesfully configured")
else:
    print("not installed")
