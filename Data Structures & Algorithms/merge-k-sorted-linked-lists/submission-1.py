# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_merged_list(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans_start = None
        ans = None
        while list1 and list2:
            smaller_node = None
            if list1.val < list2.val:
                smaller_node = list1
                list1 = list1.next
            else:
                smaller_node = list2
                list2 = list2.next
            if ans_start is None:
                ans_start = smaller_node
                ans = smaller_node
            else:
                ans.next = smaller_node
                ans = ans.next

        while list1:
            smaller_node = list1
            list1 = list1.next
            if ans_start is None:
                ans_start = smaller_node
                ans = smaller_node
            else:
                ans.next = smaller_node
                ans = ans.next

        while list2:
            smaller_node = list2
            list2 = list2.next
            if ans_start is None:
                ans_start = smaller_node
                ans = smaller_node
            else:
                ans.next = smaller_node
                ans = ans.next
            
        return ans_start

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            if lists[0] is None:
                return None

            return lists[0]

        ans = lists[0]

        for i in range(1, len(lists)):
            ans = self.get_merged_list(ans, lists[i])

        return ans
