"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
# My Solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return int(str(x)[::-1]) == x

Solution().isPalindrome(12321)
Solution().isPalindrome(123)


"""
Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

# Reference Solution
"""
The first idea that comes to mind is to convert the number into string, and check if the string is a palindrome, 
but this would require extra non-constant space for creating the string which is not allowed by the problem description.

Second idea would be reverting the number itself, and then compare the number with original number, if they are the same, 
then the number is a palindrome. However, if the reversed number is larger than int.MAX, we will hit integer overflow problem.

Following the thoughts based on the second idea, to avoid the overflow issue of the reverted number, 
what if we only revert half of the int number? 
After all, the reverse of the last half of the palindrome should be the same as the first half of the number, if the number is a palindrome.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) or ((x % 10 == 0) and (x != 0)):
            return False
        else: 
            revert = 0
            while x > revert:
                temp = x % 10
                revert = revert*10 + temp
                x = int((x-temp)/10)
        
        return x == revert or x == int((revert - revert%10)/10)
    
Solution().isPalindrome(12321)
Solution().isPalindrome(-12321)
Solution().isPalindrome(10)

# Time complexity : O(log​10n)
