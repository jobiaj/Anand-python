#cumulative product of elements in a list
a=[3,4,2,5]
b=[]
def pdt(a):
	pdt=1
	for i in a:
		pdt=pdt*i
		b.append(pdt)
	print b
pdt(a)
