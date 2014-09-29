#function for find all dups in a list
a=[2,3,1,3,5,2,7,6,8,4,7,1,2]
b=[]
c=[]
def dups(a):
	for i in a:
		if(a.count(i)>1):
			b.append(i)
		for i in b:
			if i not in c:
				c.append(i)
	print c
dups(a)
