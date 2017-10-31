"""
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return "{} <- {} -> {}".format(self.left, self.val, self.right)

class Solution(object):
    # My Solution: Recursion
    # Time:  O(n)
    # Space: O(h), h is height of binary tree
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
        
        
# Test
p, p.left, p.right = TreeNode(10), TreeNode(9), TreeNode(11)
q, q.left, q.right = TreeNode(10), TreeNode(8), TreeNode(9)
Solution().isSameTree(p, q)

p, p.left, p.right = TreeNode(10), TreeNode(9), TreeNode(11)
q, q.left, q.right = TreeNode(10), TreeNode(9), TreeNode(11)
Solution().isSameTree(p, q)