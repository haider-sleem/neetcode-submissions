# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list in-place.

        Args:
            head (Optional[ListNode]): The beginning of the singly linked list.

        Returns:
            Optional[ListNode]: The new head of the reversed linked list.
        """
        prev = None
        current = head
        
        while current is not None:
            # 1. Store the next node to avoid losing the rest of the list
            next_node = current.next
            
            # 2. Reverse the current node's pointer to point backward
            current.next = prev
            
            # 3. Move the prev pointer forward to the current node
            prev = current
            
            # 4. Move the current pointer forward to the saved next node
            current = next_node
            
        # At the end of the loop, prev points to the new head of the reversed list
        return prev

