def plusMinus(arr):
    # Write your code here
    n=len(arr)
    a,b,c=0,0,0
    for i in arr :
        if i>0:
            a+=1
        elif i<0:
            b+=1
        else :
            c +=1
    print(a/n)
    print(b/n)
    print(c/n)
