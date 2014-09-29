a=open('z.txt','r')
f=a.readlines()
b=len(max(f))
for i in f:
	c=(b-len(i))/2
	print ' '*c+i+' '*c

