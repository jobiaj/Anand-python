#minimum and maximum digit in a list
a=[5,3,8,2]
def min(a):
	m=a[0]
	for i in a[1:]:
		if m>i:
			m=i
	print m
min(a)
def max(a):
	n=a[0]
	for i in a[1:]:
		if n<i:
			n=i
	print n
max(a)
	
