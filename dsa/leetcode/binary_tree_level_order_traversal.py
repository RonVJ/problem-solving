# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        q = deque()
        q.append(root)
        q.append(None)
        ans = []
        level = []

        while len(q) != 0:
            temp = q.popleft()

            if temp is not None:
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            else:
                ans.append(level)
                level = []
                if len(q) != 0:
                    q.append(None)
        return ans
