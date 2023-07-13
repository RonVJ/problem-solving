# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        dq = deque()
        dq.append(root)
        dq.append(None)
        level = []
        ans = []
        is_odd_level = True

        while len(dq) != 0:
            if is_odd_level:
                temp = dq.popleft()
                if temp:
                    level.append(temp.val)
                    if temp.left:
                        dq.append(temp.left)
                    if temp.right:
                        dq.append(temp.right)
                else:
                    ans.append(level)
                    level = []
                    if len(dq) != 0:
                        dq.appendleft(None)
                        is_odd_level = is_odd_level ^ True
            else:
                temp = dq.pop()
                if temp:
                    level.append(temp.val)
                    if temp.right:
                        dq.appendleft(temp.right)
                    if temp.left:
                        dq.appendleft(temp.left)
                else:
                    ans.append(level)
                    level = []
                    if len(dq) != 0:
                        dq.append(None)
                        is_odd_level = is_odd_level ^ True



        return ans