"""
Write a function to find the longest common prefix string amongst an array of strings.

Example:
Input  : ["apple", "ape", "april"]
Output : "ap"
"""
# My Solution:
class Solution(object):
    def CommonPre(self, s):
        """
        :type s: list[str]
        :rtype: str
        """
        length = [len(item) for item in s]
        n = min(length)
        i = 1
        
        while i < n:
            s_1 = [item[:i] for item in s]
            if len(set(s_1)) == 1:
                i +=1
            else:
                break
            
        return s_1[0] if len(set(s_1)) == 1 else print("No Common Prefix")
        
        
        
Solution().CommonPre(["apple", "ape", "april"])
Solution().CommonPre(["apple", "cpe", "april"])



# Reference Solution:
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
#        return strs[0]      # don't get the meaning, still work without this line 
    

strs = ["hello", "heaven", "heavy"]
Solution().longestCommonPrefix(strs)
Solution().longestCommonPrefix(["apple", "cpe", "april"])
# Time:  O(n * k), k is the length of the common prefix

class Solution(object):
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
#        else:                               # # don't get the meaning, still work without this line 
#            return min(strs)   
        
strs = ["hello", "heaven", "heavy"]
Solution().longestCommonPrefix(strs)
Solution().longestCommonPrefix(["apple", "cpe", "april"])


# Time:  O(n)

# lookup = {v:i for i, v in enumerate(zip(*strs))}