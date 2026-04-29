# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def append_node(self, start, end, new_node):
        if start is None:
            return new_node, new_node

        end.next = new_node
        end = end.next

        return start, end

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start, end = None, None
        while list1 and list2:
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next

            start, end = self.append_node(start, end, node)

        while list1:
            node = list1
            list1 = list1.next
            start, end = self.append_node(start, end, node)

        while list2:
            node = list2
            list2 = list2.next
            start, end = self.append_node(start, end, node)

        return start
