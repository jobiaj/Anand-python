import os
import urllib
a='http://docs.python.org/tutorial/interpreter.html'
if a[-1]=='/':
	b=a+'index.html'
else:
	b=os.path.basename(a)
r=urllib.urlopen(a)
print b,r.headers

