"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution(object):
    # My Soution
    # Time:  O(n)
    # Space: O(1)
    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        
        while i < x:
            if i*i <= x  and (i+1)*(i+1) > x:
                break
            else:
                i += 1
        return i
    
    # Reference Solution: Binary Search
    # Time:  O(log n)
    # Space: O(1)
    def mySqrt2(self, x):
        low, high, mid = 0, x, x / 2
        while low <= high:
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) / 2
        return mid

    # Reference Solution: Newton's Method
    """
    Newton's Method is a method for finding successively better approximations to the roots (or zeroes) of a real-valued function.
    The process is repeated as:
    Xn+1 = Xn - f(Xn)/f'(Xn)
    
    f(t) = t^2 - x, sqrt(x) is the root of f(t)
    """
    def mySqrt3(self, x):
        t = x
        while t * t > x:
            t = int(t / 2.0 + x / (2.0 * t))
        return t

Solution().mySqrt1(65)
Solution().mySqrt2(65)
Solution().mySqrt3(65)
