# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def recursive_preorder_traversal(self, root, ans):
        if root is None:
            return
        ans.append(root.val)
        self.recursive_preorder_traversal(root.left, ans)
        self.recursive_preorder_traversal(root.right, ans)

    def iterative_preorder_traversal(self, root, ans):
        if root is None:
            return

        stack = deque()
        temp = root

        while temp or len(stack) != 0:
            while temp:
                ans.append(temp.val)
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            temp = temp.right

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        # self.recursive_preorder_traversal(root, ans)
        self.iterative_preorder_traversal(root, ans)
        return ans
