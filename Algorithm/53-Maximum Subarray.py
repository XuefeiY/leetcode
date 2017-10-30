"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution(object):
    # My Solution:
    # Brute Force
    # Complexity:
    # O(n^2) time
    # O(1) space
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        sub = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if sum(nums[i:j]) > temp:
                    temp = sum(nums[i:j])
                    sub = nums[i:j]
        return sub, temp


    # Reference Solution:
    # Dynamic Programming
    # Complexity:
    # O(n) time
    # O(1) space
    """
    We could use an array to record maximum subarray at each index.
    Let S[j] denote the maximum sum value among all those subarrays ended at A[j], 
    we have the recursive definition: S[j] = max(A[j], A[j] + S[j - 1]).
    """
    def maxSubArray2(self, A):
        ThisSum = 0
        MaxSum = -10000
        
        for i in range( 0, len(A)):
            if ThisSum < 0:
                ThisSum = 0
            ThisSum = ThisSum + A[i]       # maximum subarray at index i-1
            MaxSum = max(ThisSum, MaxSum)

        return MaxSum
 
    
    # Divide and Conquer
    # Complexity:
    # O(nlogn) time
    # O(logn) space
    """
    Assume we partition the array A into two smaller arrays S and T at the middle index, m. Then, S = A1 ... Am-1, and T = Am+1 ... An.

    The contiguous subarray that has the largest sum could either: 

    i. Contain the middle element: 
    The largest sum is the maximum suffix sum of L + Am + the maximum prefix sum of T. 
    (We need to find maximum subarray from middle point to two directions, to left find maximum: Ai...Am-1 and to right find maximum: Am+1...Aj. 
    So, maximum suffix sum is Ai...Aj including middle point.)
  
    ii. Does not contain the middle element:
    The largest sum is in S, which we could apply the same algorithm to S.
    The largest sum is in T, which we could apply the same algorithm to T.
    """
    def maxSubArray3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums) - 1)
        
    def helper(self, nums, l, r):
        # No element in the array
        if l > r:
            return 0
        
        m = (l + r) // 2
        left = self.helper(nums, l, m - 1)
        right = self.helper(nums, m + 1, r)
        
        # find maximum sum crossing to left
        leftMax = a = 0
        for i in range(m-1, l-1, -1):
            a += nums[i]
            leftMax = max(leftMax, a)
        
        # find maximum sum crossing to right
        rightMax = b = 0
        for i in range(m+1, r+1):
            b += nums[i]
            rightMax = max(rightMax, b)
        
        return max(leftMax + nums[m] + rightMax, max(left, right))
    
Solution().maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])
Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4])
Solution().maxSubArray3([-2,1,-3,4,-1,2,1,-5,4])
