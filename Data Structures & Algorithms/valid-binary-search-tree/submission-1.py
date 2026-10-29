# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        next_current = [(root, float("-inf"), float("inf"))]

        while next_current:
            current, low, high = next_current.pop()

            if current.val <= low or current.val >= high:
                return False

            if current.left is not None:
                next_current.append((current.left, low, current.val))

            if current.right is not None:
                next_current.append((current.right, current.val, high))
        
        return True

            
        