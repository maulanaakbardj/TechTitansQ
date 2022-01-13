def diagonalDifference(arr):
    # Write your code here
    a, b = 0, 0
    n=len(arr)
    for i in range (n) :
        a+=arr[i][i]
        b+=arr[i][n-i-1]
    return abs(a-b)
