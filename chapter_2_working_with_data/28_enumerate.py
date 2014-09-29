#function enumerate in the form of (item,index)
a=['j','o','b','y']
b=range(len(a))
def enu(a):
	return[(x,y) for x in a for y in b if a.index(x)==b.index(y)]
print enu(a)
