# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTMinMax(root, float("-inf"), float("inf"))
        

    def isValidBSTMinMax(self, node: Optional[TreeNode], low: int, high: int) -> bool:
        if node is None:
            return True

        if not (node.val > low and node.val < high):
            return False

        return self.isValidBSTMinMax(node.left, low, node.val) and self.isValidBSTMinMax(node.right, node.val, high)

