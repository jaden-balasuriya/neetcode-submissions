# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        currentNode = head.next
        prevNode = head

        while currentNode is not None:
            
            nextNode = currentNode.next

            currentNode.next = prevNode

            prevNode = currentNode

            currentNode = nextNode
        
        head.next = None
        return prevNode

            