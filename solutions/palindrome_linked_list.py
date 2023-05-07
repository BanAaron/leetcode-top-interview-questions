from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if head is empty we can just return false
        if head is None:
            return False

        # we will store the value of our nodes here
        values = list()

        # keep looping until we run our of nodes
        while head is not None:
            # append the value of the current node to our list
            values.append(head.val)
            # set the current head to be the next
            head = head.next

        # if values is the same forwards as it is backwards it is palindromic
        if values == values[::-1]:
            return True
        else:
            return False
