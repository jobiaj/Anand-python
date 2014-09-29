#sort a list based on the string length
a=['aaaa','bb','ccc','d','eeeee']
b=[]
def sort(a):
	for x in sorted(a,key=len):
		b.append(x)
	print b
sort(a)
