from itertools import combinations

def subsetA(arr):
    for i in range(1,len(arr)+1):
        # find all possible combinations of arr elements in size i
        listA=list(combinations(arr,i))
        
        # sort the items of the combination list by the sum of elements in the item
        listA=sorted(listA, key=lambda x: sum(x), reverse=True)
        
        # compare and return the subsetA where sum(subsetA)>sum(subsetB)
        for item in listA:
            if (sum(item)>(sum(arr)-sum(item))):
                return sorted(item)
