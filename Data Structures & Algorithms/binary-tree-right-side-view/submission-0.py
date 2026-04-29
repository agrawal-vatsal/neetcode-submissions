# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def set_right_side_view(self, node, depth, right_side_element):
        if node is None:
            return

        right_side_element[depth] = node.val

        self.set_right_side_view(node.left, depth + 1, right_side_element)
        self.set_right_side_view(node.right, depth + 1, right_side_element)


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_element = {}

        self.set_right_side_view(root, 1, right_side_element)

        arr = [None] * len(right_side_element)

        for k, v in right_side_element.items():
            arr[k - 1] = v

        return arr