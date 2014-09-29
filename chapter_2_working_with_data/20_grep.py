#the selection of sentences which contains the given word
x=raw_input('enter the word:')
f=open('z.txt','r')
a=f.readlines()
for i in a:
	if x in i:
		print i

