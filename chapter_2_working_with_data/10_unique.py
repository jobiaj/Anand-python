#unique values from list
a=[2,3,2,1,3,4]
b=[]
def unique(a):
	for i in a:
		if i not in b:
			b.append(i)
	print b
unique(a)
