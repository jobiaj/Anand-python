def square(x):
    return x * x
def cube(x):  
    return x*x*x
def map(f,l):
        if(f == 'square'):
            return [square(x) for x in l if f == 'square']
        if(f == 'cube'):    
            return [cube(x) for x in l if f == 'cube']
    
    

print map('square',[1,2,3,4,5])
