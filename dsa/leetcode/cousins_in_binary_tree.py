##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 993. Cousins in Binary Tree
# Problem link: https://leetcode.com/problems/cousins-in-binary-tree/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodes_on_level = [root]
        while len(nodes_on_level) != 0:
            nodes_on_next_level = []
            interesting_nodes = 0

            for node in nodes_on_level:
                interesting_children_of_parent = 0
                if (node.val == x) or (node.val == y) :
                    interesting_nodes = interesting_nodes + 1
                if node.left:
                    if (node.left.val == x) or (node.left.val == y) :
                        interesting_children_of_parent = interesting_children_of_parent + 1
                    nodes_on_next_level.append(node.left)
                if node.right:
                    if (node.right.val == x) or (node.right.val == y) :
                        interesting_children_of_parent = interesting_children_of_parent + 1
                    nodes_on_next_level.append(node.right)
                if interesting_children_of_parent == 2:
                    return False
            if interesting_nodes == 1:
                return False
            elif interesting_nodes == 2:
                return True
            nodes_on_level = nodes_on_next_level
        return False