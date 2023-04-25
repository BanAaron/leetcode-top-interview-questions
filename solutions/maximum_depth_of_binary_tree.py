# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # recursively call maxDepth() on the left and right of our node.
        # return the maximum between left and right + 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
