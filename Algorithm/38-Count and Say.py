"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
"""

# My Solution:
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            new_res, temp, count = '', res[0], 0
            for j in range(len(res)):
                if res[j] == temp:
                    count += 1
                else:
                    new_res += str(count) + temp
                    count = 1
                    temp = res[j]
            res = new_res + str(count) + temp
        return res

if __name__ == "__main__":
    for i in range(1, 6):
        print (Solution().countAndSay(i)) 

# Reference Solution:
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(1,n):
            s = self.read(s)
        return s
    
    def read(self, test):
        count = 1
        new = ''
        for i in range(len(test)):
            if i+1 < len(test) and test[i] != test[i+1]:
                new = new + str(count) + test[i]
                count  = 1
            elif i+1 < len(test):
                count +=1
        new = new + str(count) + test[i]
        return new
        
        

if __name__ == "__main__":
    for i in range(1, 6):
        print (Solution().countAndSay(i))     

# Packages needed
import itertools
class Solution(object):
    def countAndSay(self, n):
        res = '1'
        for i in range(n-1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res
    
if __name__ == "__main__":
    for i in range(1, 6):
        print (Solution().countAndSay(i))    
    
# itertools.groupby():
# It only groups the items if their key-result is the same for successive items
# One could use sorted before - if one wants to do an overall groupby.
