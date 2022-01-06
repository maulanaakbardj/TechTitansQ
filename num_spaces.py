name1='I lo ve yo u so mu ch' #name = input() 1  
name2='T  witter' #name = input() 2 
spaces=[' ']
def f (n):
    a=sum([1 for i in n if i in spaces]) 
    return a
print('%s' % f(name1)) 
print('%s' % f(name2)) 
