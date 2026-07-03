# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
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
        if head is None or head.next is None:
            return None


        #get length of list
        p = head
        length = 1

        while p.next is not None:
            p = p.next
            length+=1

        #go half way up list
        half = -(length // -2)

        p2 = head
        for i in range(half-1):
            p2 = p2.next
        tail = p2
        p2 = p2.next
        tail.next = None
        
        #reverse list
        p2 = reverseList(p2)
        p1 = head

        #mesh list
        
        while p1 is not None and p2 is not None:
            nextNode = p1.next
            p1.next = p2
            nextp2 = p2.next
            p2.next = nextNode
            p2 = nextp2
            p1 = nextNode
