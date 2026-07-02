# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = list1

        p2 = list2

        head = ListNode()

        currentNode = head

        while p1 is not None or p2 is not None:
            if p1 is None and p2 is not None:
                currentNode.next = p2
                break
            if p2 is None and p1 is not None:
                currentNode.next = p1
                break
            if p1.val < p2.val:
                currentNode.next = p1
                currentNode = p1
                p1 = p1.next
            else:
                currentNode.next = p2
                currentNode = p2
                p2 = p2.next
        
        return head.next
            