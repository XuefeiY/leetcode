"""
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example:
Input  : "aabbaa", "bb"
Output : 2
"""

class Solution(object):
    # Goal: To implement the function string.find()
    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
    # My Solution
    # Time:  O(n * k)
    # Space: O(k)
    """
    Scan the haystack, when the character at current index is the same with the first character of needle, 
    check the chunk of character with the needle's length in the haystack starting from the current index.
    If the chunk is the same with needle, return the index.
    """
    def strStr2(self, haystack, needle):      
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
    # Reference: KMP algorithm
    # Time:  O(n + k)
    # Space: O(k)
    """
    The Naive pattern searching algorithm doesn’t work well in cases where we see many matching characters followed by a mismatching character.
    
    The KMP matching algorithm uses degenerating property (pattern having same sub-patterns appearing more than once in the pattern) 
    of the pattern and improves the worst case complexity to O(n). The basic idea behind KMP’s algorithm is: whenever we detect a 
    mismatch (after some matches), we already know some of the characters in the text of next window. 
    We take advantage of this information to avoid matching the characters that we know will anyway match. 
    """
    def getPrefix(self, needle):
        prefix = [-1] * len(needle)
        j = -1
        for i in range(1, len(needle)):
            while j > -1 and needle[j + 1] != needle[i]:
                j = prefix[j]
            if needle[j + 1] == needle[i]:
                j += 1
            prefix[i] = j
        return prefix

    def KMP(self, haystack, needle):
        prefix = self.getPrefix(needle)
        j = -1
        for i in range(len(haystack)):
            while j > -1 and needle[j + 1] != haystack[i]:
                j = prefix[j]
            if needle[j + 1] == haystack[i]:
                j += 1
            if j == len(needle) - 1:
                return i - j
        return -1
    
    def strStr3(self, haystack, needle):
        if not needle:
            return 0
        return self.KMP(haystack, needle)

    
    

Solution().strStr1("aabbaa", "aba")
Solution().strStr1("aabbaa", "ab")
Solution().strStr2("aabbaa", "aba")
Solution().strStr2("aabbaa", "bb")
Solution().strStr3("abdabc", "abc")
Solution().strStr3("abdabc", "abcd")


