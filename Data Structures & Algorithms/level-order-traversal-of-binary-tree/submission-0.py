# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderWithAns(self, root: Optional[TreeNode], level: int, ans: List[List[int]]):
        if root is None:
            return

        if len(ans) < level:
            ans.append([])

        ans[level-1].append(root.val)
        self.levelOrderWithAns(root.left, level + 1, ans)
        self.levelOrderWithAns(root.right, level + 1, ans)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.levelOrderWithAns(root, 1, ans)
        return ans