# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            #Swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers forward
            prev = first
            head = first.next

        return dummy.next
    