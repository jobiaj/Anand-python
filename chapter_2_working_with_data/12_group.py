#group the numbers in a list
a=[1,2,3,4,5,6]
def group(a,n):
	i=0
	b=[]
	for j in range(len(a)/n):
		b.append(a[i:i+n])
		i=i+n
	print b
group(a,3)
