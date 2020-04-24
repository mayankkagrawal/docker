#!/usr/bin/python3.6

print('content-type: text/html')
print()

import cgi 
import subprocess

form=cgi.FieldStorage()
del1=form.getvalue('del1')

x=subprocess.getoutput(" sudo userdel {}".format(del1))
print(x)
