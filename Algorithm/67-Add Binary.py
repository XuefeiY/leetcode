"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    # My Solution: Recursion
    # undesirable time complexity using recursion
    def addBinary1(self, a, b):
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
            c = self.addBinary1(a_new, c)
            
        if n2 > n1:
            b_new = list(b[0:n2-n1])+[0]*n1
            c = self.addBinary1(b_new, c)
        return ''.join([str(item) for item in c])
    
    
    # Reference Solution:
    # Pad the strings with shorter length
    def addBinary2(self, a, b):
        length = max(len(a),len(b)) + 1
        sum = ['0' for i in range(length)]
        if len(a) <= len(b):
            a = '0' * ( len(b) - len(a) ) + a
        if len(a) > len(b):
            b = '0' * ( len(a) - len(b) ) + b
        flag = 0
        i = len(a) - 1
        while i >= 0:
            if int(a[i]) + int(b[i]) + flag == 3:
                sum[i+1] = '1'
                flag = 1
            elif int(a[i]) + int(b[i]) + flag == 2:
                sum[i+1] = '0'
                flag = 1
            elif int(a[i]) + int(b[i]) + flag == 1:
                sum[i+1] = '1'
                flag = 0
            else:
                sum[i+1] = '0'
                flag = 0
            i = i - 1
        if flag == 1:
            sum[0] = '1'
        if flag == 0:
            sum = sum[1:length]
        sum = ''.join(sum)
        return sum
    
    # Strings with different lengths
    def addBinary3(self, a, b):
        aIndex = len(a)-1; bIndex = len(b)-1
        flag = 0
        s = ''
        while aIndex>=0 and bIndex>=0:
            num = int(a[aIndex])+int(b[bIndex])+flag
            flag = num//2; num %= 2
            s = str(num) + s
            aIndex -= 1; bIndex -= 1
        while aIndex>=0:
            num = int(a[aIndex])+flag
            flag = num//2; num %= 2
            s = str(num) + s
            aIndex -= 1
        while bIndex>=0:
            num = int(b[bIndex])+flag
            flag = num//2; num %= 2
            s = str(num) + s
            bIndex -= 1
        if flag == 1:
            s = '1' + s
        return s
    
    
    
    
Solution().addBinary1('111', '101')
Solution().addBinary1('11', '1')
Solution().addBinary2('111', '101')
Solution().addBinary2('11', '1')               
Solution().addBinary3('111', '101')
Solution().addBinary3('11', '1')          

                
            
        
        
                
        
