def subsetA(arr):
    # Write your code here
    arr = sorted(arr, reverse=True)
    for i in range(1,len(arr)+1):
        if(sum(arr[:i])>sum(arr[i:])):
            subsetA = sorted(arr[:i])
            return subsetA
