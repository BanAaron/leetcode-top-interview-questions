from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Set up three pointers to traverse the linked list
        prev = None
        curr = head

        # Traverse the linked list and reverse the pointers
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Return the new head of the reversed linked list
        return prev
