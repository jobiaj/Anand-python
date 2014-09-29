#function triplet using list comprehension
def triplet(a):
	return[(x,y,z) for x in range(1,a) for y in range(x,a) for z in range(y,a) if z==x+y]
print triplet(5)
