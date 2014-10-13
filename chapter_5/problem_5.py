import os
import re
def find_number_of_py(dirr):
	d = []
	e = []
	files = os.listdir(dirr)
	for i in files:
		d.append(i.split('.'))
	#return d
	for i in files:
		special = re.search(r'.py',i)
		if special:
			e.append(i)
	
	return 'The length of the python files in the given directory =' + str(len(e))
		

print find_number_of_py('/home/jobi/Recursive/mysamples')
