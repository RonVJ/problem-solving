# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):

    def recursive_implementation(self, root, ans):
        if root is None:
            return
        self.recursive_implementation(root.left, ans)
        # print (root.val)
        ans.append(root.val)
        self.recursive_implementation(root.right, ans)

    def iterative_implementation(self, root, ans):
        stack = deque()
        temp = root

        while temp or (len(stack) != 0):
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                ans.append(temp.val)
                temp = temp.right

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        # self.recursive_implementation(root, ans)
        self.iterative_implementation(root, ans)
        return ans