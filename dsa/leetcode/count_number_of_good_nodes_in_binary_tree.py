# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def num_of_good_nodes(self, root, max_in_path):
        if root is None:
            return 0
        total_good_nodes = 0
        if root.val >= max_in_path:
            total_good_nodes = total_good_nodes + 1

        total_good_nodes = total_good_nodes + self.num_of_good_nodes(root.left, max(max_in_path, root.val))
        total_good_nodes = total_good_nodes + self.num_of_good_nodes(root.right, max(max_in_path, root.val))
        return total_good_nodes

    def goodNodes(self, root: TreeNode) -> int:
        inf = sys.maxsize
        return self.num_of_good_nodes(root, -inf)