# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    MAX_DEPTH = 0

    def get_depth(self, node, depth):
        if node is None:
            return

        self.MAX_DEPTH = max(self.MAX_DEPTH, depth)

        self.get_depth(node.right, depth + 1)
        self.get_depth(node.left, depth + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.MAX_DEPTH = 0
        self.get_depth(root, 1)
        return self.MAX_DEPTH