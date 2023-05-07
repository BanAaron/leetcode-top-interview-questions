from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []

        # this following "while True" block keeps running until "return"
        while True:
            # goes all the way to left end's None, append every step onto "stack"
            while root:
                stack.append(root)
                root = root.left

            # if stack has nothing left, then return result
            if not stack:
                return res

            # take the last step out, append its value to result
            node = stack.pop()
            res.append(node.val)
            # moves to right before going all the way to left end's None again
            root = node.right
