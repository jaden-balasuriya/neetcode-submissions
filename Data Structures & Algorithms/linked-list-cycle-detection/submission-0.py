# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        toggle = False

        while fast is not None:
            fast = fast.next
            if fast is slow:
                return True
            if toggle:
                slow=slow.next
            toggle = not toggle
        return False


