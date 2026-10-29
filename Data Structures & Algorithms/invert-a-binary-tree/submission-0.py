# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        next_current = [root]

        while next_current:
            current = next_current.pop()

            # Swap left and right children
            current.left, current.right = current.right, current.left

            # Save children that still need processing
            if current.left is not None:
                next_current.append(current.left)

            if current.right is not None:
                next_current.append(current.right)

        return root
