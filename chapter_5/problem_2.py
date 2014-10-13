def cat(filenames):
	for f in filenames:
		for line in open(f):
			if len(line)>40:
				yield line
c = cat(['2.txt','1.txt'])
for i in c:
	print i 

