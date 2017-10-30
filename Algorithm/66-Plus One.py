"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    # My Solution:
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 0
        for i in range(len(digits)):
            res = res*10
            res += digits[i]
        res += 1
        return [int(item) for item in list(str(res))]
    
    # Reference Solution:
    def plusOne2(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits   
    
    
Solution().plusOne1([1,2,3,4])
Solution().plusOne2([9,9,9,9]) 

    