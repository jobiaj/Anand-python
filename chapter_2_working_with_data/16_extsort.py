a=['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
b=[]
c=[]
x=[]
y=[]
def extsort(a):
	for i in a:
		x.append(i.split("."))
	j=0
	for k in x:
		b.append(x[j][0])
		c.append(x[j][1])
		j=j+1
	m=zip(c,b)
	m.sort()
	l=0
	for q in m:
		y.append('.'.join([m[l][1],m[l][0]]))
		l=l+1
	print y
extsort(a)
