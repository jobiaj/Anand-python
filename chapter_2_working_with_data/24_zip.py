def zip(a,b):
    print [(x,y) for x in a for y in b if a.index(x) == b.index(y)]

zip([1,2,3],['g','s','d'])
