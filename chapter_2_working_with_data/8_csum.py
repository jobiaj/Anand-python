#cumulative sum of a list
x=[1,2,3,4]
y=[]
def csum(x):
	for i in x:
		i=sum(range(0,i+1))
		y.append(i)
	print y
csum(x)
