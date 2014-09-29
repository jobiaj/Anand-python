#reverse a list
w=[2,4,5,9]
i=len(w)
r=range(i,0,-1)
q=[]
for j in r:
	q.append(w[j-1])
print q
