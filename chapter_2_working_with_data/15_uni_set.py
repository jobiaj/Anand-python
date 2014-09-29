#implementation of unique function in set
a=(2,3,1,6,4,3,2)
b=[]
def uni(a):
	for i in a:
		if i not in b:
			b.append(i)
	print b
uni(a)
