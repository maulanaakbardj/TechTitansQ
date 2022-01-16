class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array = [nums1, nums2]
        total = sum(len(nums) for nums in array)
        if total % 2 == 1:
            return self.getKth(array, total//2 + 1)
        else:
            return (self.getKth(array, total//2) +
                    self.getKth(array, total//2 + 1)) * 0.5

    def getKth(self, arrays, k):
        def binary_search(array, left, right, target, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(array, mid, target):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def check(arrays, num, target):
            res = 0
            for array in arrays:
                if array:  # count the number of values which are less or equal to num
                    res += binary_search(array, 0, len(array) - 1, num,
                                         lambda array, x, y: array[x] > y)
            return res >= target

        left, right = float("inf"), float("-inf")
        for array in arrays:
            if array:
                left = min(left, array[0])
                right = max(right, array[-1])
        return binary_search(arrays, left, right, k, check)
