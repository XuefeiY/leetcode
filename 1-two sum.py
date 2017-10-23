# =============================================================================
# # 1. Two Sum
# =============================================================================
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# My Solution
# Method 1      
def twoSum1(nums, target):
    for i in range(len(nums)):
        temp = target - nums[i]
        for j in range(len(nums)):
            if nums[j] == temp:
                return[i,j]
                
                
nums = [2, 7, 11, 2, 15]
target = 9
twoSum1(nums, target)              
# time complexity: O(n^2)


# Method 2
def twoSum2(nums, target):
   for item in nums:
       temp = target - item
       if temp in nums:
           return [nums.index(item), nums.index(temp)]
       else:
           return 'NA'

nums = [2, 7, 11, 2, 15]
target = 9
twoSum2(nums, target) 
# time complexity: O(n)


# Reference Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = dict(((v, i) for i, v in enumerate(nums)))
        for i, v in enumerate(nums):
            if lookup.get(target - v):
                return [i, lookup.get(target - v)]

Solution().twoSum([2, 7, 11, 2, 15], 9)
# time complexity: O(n)




        