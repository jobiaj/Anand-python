def count_v(s):
    	v = list('aeiou')
	b = list(s)
	count = 0
	for i in b:
     		if i in v:
           		count=count + 1
	return count

print count_v('tknidigygiqppaywdgxodelh')
