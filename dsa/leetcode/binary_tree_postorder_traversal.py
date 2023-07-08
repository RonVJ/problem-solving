# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):

    def recursive_postorder_traversal(self, root, ans):
        if root is None:
            return
        self.recursive_postorder_traversal(root.left, ans)
        self.recursive_postorder_traversal(root.right, ans)
        ans.append(root.val)

    def iterative_postorder_traversal(self, root, ans):
        temp = root
        stack = deque()

        while temp or len(stack)!=0 :
            while(temp):
                stack.append(temp)
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            if (len(stack) != 0) and (temp == stack[-1]):
                temp = temp.right
            else:
                ans.append(temp.val)
                temp = None


    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        # self.recursive_postorder_traversal(root, ans)
        self.iterative_postorder_traversal(root, ans)
        return ans
