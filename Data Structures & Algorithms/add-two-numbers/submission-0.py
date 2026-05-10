# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_l1, node_l2 = l1, l2
        carry = 0
        sum_list = None
        sum_node = None

        while node_l1 and node_l2:
            total_val = node_l1.val + node_l2.val + carry
            sum_val = total_val % 10
            carry = total_val // 10
            new_node = ListNode(sum_val)
            if sum_list is None:
                sum_node = new_node
                sum_list = sum_node
            else:
                sum_node.next = new_node
                sum_node = sum_node.next

            node_l1 = node_l1.next
            node_l2 = node_l2.next

        while node_l1:
            total_val = node_l1.val + carry
            sum_val = total_val % 10
            carry = total_val // 10
            new_node = ListNode(sum_val)
            sum_node.next = new_node
            sum_node = sum_node.next
            node_l1 = node_l1.next

        while node_l2:
            total_val = node_l2.val + carry
            sum_val = total_val % 10
            carry = total_val // 10
            new_node = ListNode(sum_val)
            sum_node.next = new_node
            sum_node = sum_node.next
            node_l2 = node_l2.next

        if carry > 0:
            new_node = ListNode(1)
            sum_node.next = new_node

        return sum_list
