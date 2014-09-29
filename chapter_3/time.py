import os
import time
f='/home/jobi/anand-python/chapter_3'
a=os.listdir(f)
for i in a:
	x=os.path.getsize(i)
	y=os.path.getatime(i)
	print i,x,y
