from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        
        deck = deque()
        cur = head

        while cur is not None:
            deck.append(cur)
            cur = cur.next
        
        cur = deck.popleft()

        while deck:
            cur.next = deck.pop()
            cur = cur.next

            if deck:
                cur.next = deck.popleft()
                cur=cur.next
        
        cur.next = None
        return

            
        