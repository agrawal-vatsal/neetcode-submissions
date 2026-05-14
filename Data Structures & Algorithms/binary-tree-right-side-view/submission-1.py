# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_traversal_marking_right_side(self, root: Optional[TreeNode], depth: int, arr: List[int]) -> None:
        if root is None:
            return

        while len(arr) < depth:
            arr.append(0)

        self.tree_traversal_marking_right_side(root.left, depth + 1, arr)
        arr[depth - 1] = root.val
        self.tree_traversal_marking_right_side(root.right, depth + 1, arr)
        

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       arr = []
       self.tree_traversal_marking_right_side(root, 1, arr)
       return arr
