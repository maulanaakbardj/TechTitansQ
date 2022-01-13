def compareTriplets(a, b):
    # Write your code here
    aa=0
    bb=0
    for i in range(len(a)):
        if a[i] > b[i]:
            aa += 1
        elif a[i] < b[i] :
            bb += 1
    return aa,bb
