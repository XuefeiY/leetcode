"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.
"""
# My Solution    
"""
Start pointer i from 0, compare nums[i] with its next one. If the same, pop out nums[i], if different, i=i+1.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return len(nums)
        
        
Solution().removeDuplicates([1,1,2,3,4,4])
Solution().removeDuplicates([1,1,1,3,3,4,4])   
Solution().removeDuplicates(None)

# Time complextiy : O(n)

# Space complexity : O(1)




# Reference Solution:
"""
Using a pointer j, when i traverse the array and meet an element different from A[j], swatch A[i] and A[j], j=j+1. 
Then i proceed to traverse the array.
"""
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates2(self, A):
        if not A:
            return 0

        j = 0

        for i in range(1, len(A)):
            if A[i] != A[j]:    # A[j] is the element to be compared, A[i] is the current element during traverse
                j += 1
                A[i], A[j+1] = A[j+1], A[i]]

        return j + 1
    
Solution().removeDuplicates2([1,1,2,3,4,4])
Solution().removeDuplicates2([1,1,1,3,4,4])
