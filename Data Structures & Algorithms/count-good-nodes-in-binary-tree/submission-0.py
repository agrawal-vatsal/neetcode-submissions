# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.goodNodesCalc(root, float("-inf"))
        return self.ans

    def goodNodesCalc(self, node: TreeNode, maxTillNow: int):
        if node is None:
            return

        if node.val >= maxTillNow:
            self.ans += 1
        
        self.goodNodesCalc(node.left, max(node.val, maxTillNow))
        self.goodNodesCalc(node.right, max(node.val, maxTillNow))