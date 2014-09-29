f={'a':2,'d':5,'c':3,'b':8}
b={}
def sort(f):
	for i,j in f.items():
		b[j]=i
	print b
print sort(f)
