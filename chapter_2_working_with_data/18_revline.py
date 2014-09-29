a=open('z.txt','r')
f=a.readlines()
def rev(a):
	for i in f:
		print i[::-1]
		
rev(a)
