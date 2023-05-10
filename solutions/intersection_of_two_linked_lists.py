from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, head_a: ListNode, head_b: ListNode
    ) -> Optional[ListNode]:
        seen: set[ListNode] = set()
        current = head_a

        # store all the nodes in headA
        while current:
            seen.add(current)
            current = current.next

        current = head_b
        while current:
            # if we find a node we have already seen, we can return it
            if current in seen:
                return current
            current = current.next

        # if we escape the while loop, it means we have no matching nodes and can return None
        return None
