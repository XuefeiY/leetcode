# =============================================================================
# 7. Reverse Integer
# =============================================================================
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

# My Solution
class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        if str(num)[0] == "-":
            new = ['-']
            num = int(str(num)[1:])
        else:
            new = []
        
        for i in range(len(str(num))):
            temp = int(num % 10)
            new.append(str(temp))
            num = (num - temp) / 10
            
        new  = ''.join(new)
        return int(new)
  
# time complexity: O(n)
Solution().reverse(-123456)   


# Reference Solution:
class Solution(object):
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x
  
# time complexity: O(logn)
Solution().reverse2(-123456) 
Solution().reverse2(1000000003) 
