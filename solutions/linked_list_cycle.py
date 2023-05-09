from typing import Optional


# ListNode definition
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we will store all the nodes we see in this list
        seen: list[ListNode] = []

        # while head is not None
        while head:
            # check if we have seen the node yet
            if head in seen:
                # if we have return True because it is a cycle
                return True
            # add the current node to our seen list
            seen.append(head)
            # set head to the next node in the link
            head = head.next

        # if we manage to break our of the loop, it means we have no nodes left and do not have a cycle
        return False
