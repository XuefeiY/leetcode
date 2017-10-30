"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""

class Solution(object):
    # My Solution:
    # Time:  O(n)
    # Space: O(n)
    def lengthOfLastWord1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[-1] == ' ':
            return 0
        else:
            return len(s.split()[-1])
        
    # Reference Solution:
    # Time:  O(n)
    # Space: O(1)
    def lengthOfLastWord2(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length
            
Solution().lengthOfLastWord1("Hello World")
Solution().lengthOfLastWord2("Hello World")