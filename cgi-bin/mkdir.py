#!/usr/bin/python3.6

print('content-type: text/html')
print()

import cgi 
import subprocess

form=cgi.FieldStorage()
dir=form.getvalue('dir')

x=subprocess.getoutput("sudo mkdir /root/{}".format(dir))
print(x)
