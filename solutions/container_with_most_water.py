class Solution:
    def maxArea(self, height: list[int]) -> int:
        # create a left and right pointer
        left = 0
        right = len(height) - 1
        area: int = 0

        # keep looping until our window is completely closed
        while left < right:
            # set area to be the max between the current value of `area` and the current value
            area = max(area, (right - left) * min(height[left], height[right]))
            # if the left side of our container is smaller than the right, then we should move onto the next from the
            # left
            if height[left] < height[right]:
                left += 1
            # in the case, that right side is less than the left then we should move on from the right
            else:
                right -= 1

        return area
