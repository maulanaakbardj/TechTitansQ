class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        for cnt, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target-num], cnt
            lookup[num] = cnt   
