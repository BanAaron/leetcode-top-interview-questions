class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        new_list = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next

            new_list = new_list.next

        if list1 is not None:
            new_list.next = list1
        else:
            new_list.next = list2

        return dummy.next
