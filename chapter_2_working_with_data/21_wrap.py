
f=open('z.txt','r')
a=f.readlines()
def wrap(a,n):
	for i in a:
		m=0
		for j in a:
			print(i[m:m+n])
			m=m+n
wrap(a,25)
