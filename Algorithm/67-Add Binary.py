"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    # My Solution: Recursion
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = len(a)
        n2 = len(b)
        n = min(n1, n2)
        c = [0]*(n+1)
        temp = 0       # carry flag
        
        # for the part with the same length
        for i in range(n):    # start from the last digit
            if int(a[n1-1-i]) + int(b[n2-1-i]) + temp >= 2:
                c[len(c)-1-i] = int(a[n1-1-i]) + int(b[n2-1-i]) + temp - 2
                temp = 1
            else:
                c[len(c)-1-i] = int(a[n1-1-i]) + int(b[n2-1-i])
                temp = 0
        # the first digit of the sum       
        if temp == 1:
            c[0] = 1      # carry bit
        else:
            c = c[1:]     # no carry bit
    
    
        # for the part with longer length
        if n1 > n2:
            a_new = list(a[0:n1-n2])+[0]*n2
            c = self.addBinary(a_new, c)
            
        if n2 > n1:
            b_new = list(b[0:n2-n1])+[0]*n1
            c = self.addBinary(b_new, c)
        return c
    
Solution().addBinary('111', '101')
Solution().addBinary('11', '1')
                
            

                
            
        
        
                
        
