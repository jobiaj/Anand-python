a=open('a.csv','r')
f=a.readlines()
b=[]
s=[]
def parse_csv(a):
	for i in f:
		b.append(i.split(','))
	print b
parse_csv(a)
