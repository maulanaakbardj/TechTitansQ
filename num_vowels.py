name1='Microsoft' #name = input() 1  
name2='Ajoyasdsforeverwqalone.' #name = input() 2 
vowels=['a','i', 'u','e', 'o', 'A','I', 'U','E', 'O']
def f (n):
    a=sum([1 for i in n if i in vowels]) 
    return a
print('%s' % f(name1))
print('%s' % f(name2)) 
