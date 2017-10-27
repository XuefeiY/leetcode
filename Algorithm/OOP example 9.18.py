# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:39:57 2017

@author: xuefei.yang
"""
# Classes and Object Orientied Programming

# =============================================================================
# # Example 1: __init__
# =============================================================================
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance


# Remark:
# 1. self is the instance of the Customer that withdraw is being called on
# 2. After __init__, we consider the Customer object "initialized" and ready for use
# 3. The rule of thumb is, don't introduce a new attribute outside of the __init__ method, 
# otherwise you've given the caller an object that isn't fully initialized.

 
# =============================================================================
# # Example 2: main()
# =============================================================================
class AnimalActions:
    def quack(self): return self.strings['quack']
    def bark(self): return self.strings['bark']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        bark = "The duck cannot bark.",
    )

class Dog(AnimalActions):
    strings = dict(
        quack = "The dog cannot quack.",
        bark = "Arf!",
    )

def in_the_doghouse(dog):
    print(dog.bark())

def in_the_forest(duck):
    print(duck.quack())

def main():
    donald = Duck()
    fido = Dog()

    print("- In the forest:")
    for o in ( donald, fido ):
        in_the_forest(o)

    print("- In the doghouse:")
    for o in ( donald, fido ):
        in_the_doghouse(o)

if __name__ == "__main__": main()

# Summary: if __name__ == '__main__': has two primary use cases:
# 1. Allow a module to provide functionality for import into other code while also providing useful semantics as a standalone script 
# (a command line wrapper around the functionality)
# 2. Allow a module to define a suite of unit tests which are stored with (in the same file as) the code to be tested and which can be 
# executed independently of the rest of the codebase.



# =============================================================================
# # Exercise 1: is Palindrome
# =============================================================================
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


Solution().isPalindrome(234)      # Solution() is an instance
Solution().isPalindrome(232)



# =============================================================================
# # Exercise 2: Valid parenthese
# =============================================================================
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

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



# =============================================================================
# # Exercise 3: Merge Two Sorted Lists
# =============================================================================
# Time:  O(n)
# Space: O(1)
#
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.
#

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):        # initialize
        self.val = x
        self.next = None
    def __repr__(self):           # representation     
        if self:
            return "{} -> {}".format(self.val, self.next)
# __repr__ should return a printable representation of the object, most likely one of the ways possible to create this object.


class Solution(object):
    # iteratively
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2    # Works if the length of l1 and l2 differ?
        return dummy.next       # remove the 0
    
    
#    x and y returns true if both x and y are true.
#    x or y returns if either one is true.


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l2 = ListNode (1)
    l2.next = ListNode(3)
    print (Solution().mergeTwoLists(l1, l2))        
        
           
# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
# in-place, iteratively        
def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

# =============================================================================
# # Exercise 4: Length of Last Word
# =============================================================================
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)-1
        while L >= 0 and s[L] == " ":
            L -= 1
        s = s[0:L+1]
        foo = s.split(" ")[-1]
        return len(foo) if s else 0
        
Solution().lengthOfLastWord("Hello World")   
Solution().lengthOfLastWord("Hello World  ")
Solution().lengthOfLastWord(" ")  
     
       
# Without using split()
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        L=len(s)-1
        while L >= 0 and s[L]==' ':
            L -= 1
        L += 1    # length of the string after removing the blanks at the most right side
        i = L - 1
        while i>= 0:
            if s[i]==' ':
                break
            i -=1
        if i < 0:
            return L
        return L-i-1 

Solution().lengthOfLastWord("Hello World")   
Solution().lengthOfLastWord("Hello World  ")
Solution().lengthOfLastWord(" ")  



# =============================================================================
# # Exercise 5: Climbing Stairs
# =============================================================================
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

# My Solution:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [1,2]
        i = 2
        while i <= n-1:
            s.append(s[i-2]+s[i-1])
            i += 1
        return s[i-1] if n > 1 else s[0]
    
Solution().climbStairs(6) 
Solution().climbStairs(10)


# Reference:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp = [0 for __ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]

Solution().climbStairs(6) 
Solution().climbStairs(10)



# =============================================================================
# # Exercise 6: Rotate Array
# =============================================================================
# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return nums[k:] + nums[:k]
    
Solution().rotate([1,2,3,4,5,6,7], 3)
