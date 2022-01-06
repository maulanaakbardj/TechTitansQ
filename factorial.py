name1='3' #name = input() 1  
name2='6' #name = input() 2 
name1=int(name1)
name2=int(name2)
def f (n):
    if n == 0 :
        return 1
    else:
        return n * f (n - 1)
print('%s' % f(name1)) 
print('%s' % f(name2)) 
