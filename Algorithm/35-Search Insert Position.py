"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    # My Solution:
    # Time Complexity: O(n)
    def searchInsert1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i <= len(nums):
            if i == len(nums):
                break
            if nums[i] < target:
                i += 1
            else:
                break         
        return i
    
    # Reference Solution: binary search
    # Time Complexity: O(log n)
    def searchInsert2(self, nums, target):
        left = 0; right = len(nums) - 1
        while left <= right:
            mid = ( left + right ) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left    
    
        
Solution().searchInsert2([1,3,5,6], 5)
Solution().searchInsert2([1,3,5,6], 2)
Solution().searchInsert1([1,3,5,6], 7)               
Solution().searchInsert1([1,3,5,6], 0)           
