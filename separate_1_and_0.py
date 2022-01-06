name1='1100111' #name = input() 1  
name2='0000110101010101010010101011111100001010' #name = input() 2 
def f (n):
    a= sorted(n, reverse=True)
    return a
arr1=f(name1)
arr2=f(name2)
def list2Str(n):
    str1=""
    for i in n :
        str1 += i
    return str1
print('%s' % list2Str(arr1)) 
print('%s' % list2Str(arr2)) 
