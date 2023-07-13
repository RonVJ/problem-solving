# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_if_valid_BST(self, root, range_left, range_right):
        if root is None:
            return True
        if not (root.val >= range_left and root.val < range_right):
            return False
        return self.check_if_valid_BST(root.left, range_left, root.val) and self.check_if_valid_BST(root.right, root.val+1, range_right)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_if_valid_BST(root, -sys.maxsize, sys.maxsize)