#!/usr/bin/python3.6

print('content-type: text/html')
print()

import cgi 
import subprocess

form=cgi.FieldStorage()
user=form.getvalue('user')

x=subprocess.getoutput(" sudo useradd {}".format(user))
print(x)
