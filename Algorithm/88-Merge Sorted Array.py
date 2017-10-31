"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
class Solution(object):
    # My Solution: three index
    # Time:  O(n)
    # Space: O(1)
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p, q, k = m-1, n-1, m+n-1     # or use 2 index, make k = p+q+1
        
        while p > -1 and q > -1:
            if nums1[p] >= nums2[q]:
                nums1[k] = nums1[p]
                p, k = p-1, k-1
            else:
                nums1[k] =nums2[q]
                q, k = q-1, k-1

        nums1[:k+1] = nums2[:q+1]     # if n > m, do it, if n <= m, nums[:k+1] should be kept as original 
        


A = [2, 3, 5, 0, 0, 0, 0]
B = [1, 4, 6, 7]
Solution().merge(A, 3, B, 4)
print (A)
