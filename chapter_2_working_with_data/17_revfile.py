#reverse of a file content
def reverse(z):
	for i in reversed(open(z).readlines()):
		print i
reverse('z.txt')
