#!/usr/bin/python3.6

print('content-type: text/html')
print()

#import cgi 
import os
import subprocess
#form=cgi.FieldStorage()
#user=form.getvalue('user')

x=subprocess.getstatusoutput('sudo yum install openssh-server openssh-clients -y')
if x[0]==0:

    os.system('sudo ossh-keygen -A')
    os.system('sudo /usr/sbin/sshd')
    print('Successfully configured')
else:
    print("not installed")
