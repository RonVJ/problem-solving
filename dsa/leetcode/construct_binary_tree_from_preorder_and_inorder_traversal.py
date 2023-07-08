# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def build_tree_from_inorder_and_preorder(self, inorder, preorder, dictionary, ins, ine, prs, pre):
        if ins > ine:
            return None
        root_val = preorder[prs]
        root_index = dictionary[root_val]
        root = TreeNode(root_val)

        num_nodes_in_left_subtree = root_index - ins
        num_nodes_in_right_subtree = ine - root_index

        root.left = self.build_tree_from_inorder_and_preorder(inorder, preorder, dictionary
                                                              , ins, root_index-1, prs+1, prs+num_nodes_in_left_subtree)

        root.right = self.build_tree_from_inorder_and_preorder(inorder, preorder, dictionary
                                                               , root_index+1, ine, pre-num_nodes_in_right_subtree+1, pre)
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        n = len(preorder)
        if n == 0:
            return None

        dictionary = {}
        for i in range(n):
            dictionary[inorder[i]] = i

        root = self.build_tree_from_inorder_and_preorder(inorder, preorder, dictionary, 0, n-1, 0, n-1)
        return root