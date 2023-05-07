from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        # if nums is empty we can return nothing
        if not nums:
            return None

        # find the middle element of the list
        middle = len(nums) // 2

        # create a root node using the middle value
        root_node = TreeNode(nums[middle])

        # create the left of the tree using the all the numbers up to the middle of the nums list
        root_node.left = self.sortedArrayToBST(nums[:middle])

        # same for the right but starting from the middle and going forwards
        root_node.right = self.sortedArrayToBST(nums[middle + 1 :])

        return root_node


if __name__ == "__main__":
    s = Solution()
    s.sortedArrayToBST([-10, -3, 0, 5, 9])
