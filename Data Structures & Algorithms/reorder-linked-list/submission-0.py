# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return 
        current = head
        located = []
        while current is not None:
            located.append(current)
            current = current.next
        n = len(located)
        left = 0
        right = n - 1
        reordered = []
        while left <= right:
            reordered.append(located[left])
            if left != right:
                reordered.append(located[right])
            left += 1
            right -= 1

        m = len(reordered)
        for i in range(m):
            if i != m - 1:
                reordered[i].next = reordered[i+1]
        reordered[i].next = None
        
            
            



