"""
21. Merge Two Sorted Lists
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.



MY OWN CODE: 
________________________________________________________________________________________________
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        Counter = 0 
        list1_pointer = 0
        list2_pointer = 0
        merged = []



        while list1_pointer < len(list1) and list2_pointer < len(list2):

            if list1[list1_pointer] <= list2[list2_pointer]:
                merged.append(list1[list1_pointer])
                list1_pointer += 1
            else:
                merged.append(list2[list2_pointer])
                list2_pointer += 1


        if list1_pointer < len(list1):
            merged.extend(list1[list1_pointer:])
        elif list2_pointer < len(list2):
            merged.extend(list2[list2_pointer:])

        return merged
    
TEST : 

test1 = [1,3,4]
test2 = [1,2,5]
sol = Solution()
print(sol.mergeTwoLists(test1, test2))
________________________________________________________________________________________________


Chat GPT: 

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode()
        # This pointer will move along the merged list as we build it
        current = dummy

        # Loop until either list1 or list2 runs out
        while list1 and list2:
            # Compare the current values of both lists
            if list1.val <= list2.val:
                # Attach the smaller node to the merged list
                current.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # Attach the smaller node to the merged list
                current.next = list2
                # Move to the next node in list2
                list2 = list2.next
            # Move the current pointer forward in the merged list
            current = current.next

        # At this point, at least one list is exhausted.
        # Directly append the remaining part of the non-empty list.
        current.next = list1 if list1 else list2

        # Return the merged list, skipping the dummy head
        return dummy.next
