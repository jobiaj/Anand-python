class reverse_iter(object):
    def __init__(self, n):
        self.i = 0
        self.n = n
	self.c = len(n)

    def __iter__(self):
        return self

    def next(self):
	b = self.n[::-1]
	for j in b:
        	if self.i<self.c:
        		return j
			self.i +=1
		else:
			raise StopIteration()
			

it = reverse_iter([1, 2, 3, 4])
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()

