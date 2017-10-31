"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    # My Solution:
    def list_to_link(self, lst):
        if len(lst) == 1:
            return ListNode(lst[0])
        new = ListNode(lst[0])
        new.next = self.list_to_link(lst[1:])
        return new
    
    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = []
        while head:
            new_head.append(head.val)
            head = head.next
        new_head = list(set(new_head))
        return self.list_to_link(new_head)
    
    # Reference Solution:
    """
    Use dummy node like 21-Merge Two Sorted Lists
    """
    # One by one
    def deleteDuplicates2(self, head):
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
    
    # Three Pointers
    # 1. Build pointer p which will traverse the whole linked list
    # 2. Build pointer q which will traverse node after p, and compare it with p
    # 3. Build pointer head which keeps nodes who need removal, and concatenate its back and forth
    def deleteDuplicates3(self, head):
        p = q = head
        while p:
            while q and q.val== p.val:
                q = q.next
            p.next = q
            p = q
        return head
     
    # Recursion
    def deleteDuplicates4(self, head):
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates4(head.next)
        return head if head.val != head.next.val else head.next          
    

    
 # Test   
Node = ListNode(1)
Node.next = ListNode(1)
Node.next.next = ListNode(2)
Node.next.next.next = ListNode(3)
Node.next.next.next.next = ListNode(3)
Node
Solution().deleteDuplicates1(Node)
Solution().deleteDuplicates2(Node)
Solution().deleteDuplicates3(Node)
Solution().deleteDuplicates4(Node)
