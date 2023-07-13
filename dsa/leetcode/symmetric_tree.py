# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_if_symmetric(self, root_left, root_right):
        if root_left is None and root_right is None:
            return True
        elif root_left is not None and root_right is not None:
            if root_left.val == root_right.val:
                return self.check_if_symmetric(root_left.left, root_right.right) and self.check_if_symmetric(root_left.right, root_right.left)

        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.check_if_symmetric(root.left, root.right)