# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self):
        self.curr = 1
        self.ans = None

class Solution:
    def kthSmallestItem(self, root, k, node):
        if root is None:
            return

        self.kthSmallestItem(root.left, k, node)
        if node.curr == k:
            node.ans = root.val
        node.curr += 1
        self.kthSmallestItem(root.right, k, node)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = Node()
        self.kthSmallestItem(root, k, node)
        return node.ans