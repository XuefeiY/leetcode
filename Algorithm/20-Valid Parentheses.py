"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
# My Solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {'(':')', '{':'}', '[':']'}
        i = 0
        while i < len(s):
            if lookup[s[i]] == s[i+1]:
                i += 2
            else:
                break
        return True if i == len(s) else False
            
Solution().isValid("()[]{}")
Solution().isValid("(]")      
Solution().isValid("()[{]}")   
# Didn't consider empty string 
        

# Reference Solution:
class Solution:
    # @return a boolean
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:  #  The method pop() removes and returns last object or obj from the list.
                return False
        return len(stack) == 0
    
if __name__ == "__main__":
    print (Solution().isValid("()[]{}"))
    print (Solution().isValid("()[{]}"))
    
    