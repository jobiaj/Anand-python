#lambda operator
def fxy(f,x,y):
	return f(x)+f(y)
cube=lambda x:x**3
print fxy(cube,2,3)
