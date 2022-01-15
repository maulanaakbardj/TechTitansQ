import heapq
def minSum(num, k):
    # Write your code here
    heap = [-n for n in num]  # negate values for max-heap
    heapq.heapify(heap)

    for i in range(k):
        max_value = heap[0]
        heapq.heapreplace(heap, math.floor(max_value/2))

    # Calculate minimum sum
    return -sum(heap)
