# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Input: head = [1,2,2,1]
# Output: true

# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # consider bounds
        # empty or list with only one node is palindrome
        if not head or not head.next:
            return True
        
        # using fast and slow pointers, find middle node
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half of the list
        # previous will be the head of the reversed list
        previous = None
        while slow:
            slow.next, slow, previous = previous, slow.next, slow
        
        # now compare the first half to the second half
        first = head
        second = previous
        
        while first and second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        
        return True
        