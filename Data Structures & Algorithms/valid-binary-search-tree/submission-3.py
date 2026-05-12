# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTMinMax(root)[0]
        

    def isValidBSTMinMax(self, node: Optional[TreeNode]):
        if node is None:
            return True, None, None

        if node.left and node.left.val >= node.val:
            return False, None, None

        if node.right and node.right.val <= node.val:
            return False, None, None

        result_left, min_left, max_left = self.isValidBSTMinMax(node.left)
        result_right, min_right, max_right = self.isValidBSTMinMax(node.right)

        if not (result_left and result_right):
            return False, None, None

        if min_right is not None and node.val >= min_right:
            return False, None, None

        if max_left is not None and node.val <= max_left:
            return False, None, None

        return True, min_left if min_left is not None else node.val, max_right if max_right is not None else node.val


