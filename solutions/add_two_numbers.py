from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # we will store each total as a string
        t1_total = ""
        t2_total = ""

        # start with l1
        node = l1
        while node:
            # adding each value onto the end of the string to form the number
            t1_total += str(node.val)
            node = node.next

        # do the same with l2
        node = l2
        while node:
            t2_total += str(node.val)
            node = node.next

        # reverse our strings, add them together as integers and then convert to list
        result = list(str(int(t1_total[::-1]) + int(t2_total[::-1]))[::-1])
        # return our list converted to a linked list
        return list_to_linked_list(result)


# accepts a list and returns a linked list
def list_to_linked_list(lst):
    """
    :param lst: list of numbers that you would like to create a linked list from
    :return: A linked list
    """
    current = dummy_node = ListNode(0)
    for e in lst:
        current.next = ListNode(e)
        current = current.next
    return dummy_node.next
