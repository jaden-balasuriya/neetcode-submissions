# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #get length
        count = 1
        p = head
        while p.next:
            count+=1
            p = p.next
        
        index = count - n
        if index == 0:
            return head.next
        
        
        p = head
        for i in range(index-1):
            p = p.next
        p.next = p.next.next

        return head