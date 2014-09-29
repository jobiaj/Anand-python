a=open('a.txt','r')
f=a.readlines()
b=[]
for i in f:
	b.append(i.split('!'))
print b
