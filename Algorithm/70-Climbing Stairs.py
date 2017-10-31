"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

class Solution(object):
    # My Solution: Recursion
    # undesirable time complexity using recursion?
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n == 1:
            res = 1
        elif n == 2:
            res = 2
        else:
            res = self.climbStairs1(n-1) + self.climbStairs1(n-2)
        return res
    
    # Reference Solution: Dynamic Programming
    # f(n) = f(n-1)+f(n-2)
    def climbStairs2(self, n):
        dp = [1 for i in range(n+1)]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]    
    
    # Fibonacci sequence
    def climbStairs3(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre+cur
        return cur    
    
Solution().climbStairs1(5)
Solution().climbStairs2(5)
Solution().climbStairs3(5)        
