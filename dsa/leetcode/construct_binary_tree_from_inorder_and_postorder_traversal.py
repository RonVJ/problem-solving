# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def build_tree_using_inorder_postorder(self, inorder, postorder, dictionary, ios, ine, pos, poe):
        if ios > ine:
            return None
        root_val = postorder[poe]
        root = TreeNode(root_val)
        root_index = dictionary[root_val]
        num_elems_right_subtree = ine - root_index
        num_elems_left_subtree = root_index - ios

        root.left = self.build_tree_using_inorder_postorder(inorder, postorder, dictionary
                                                            , ios, root_index-1, pos, pos+num_elems_left_subtree-1)

        root.right = self.build_tree_using_inorder_postorder(inorder, postorder, dictionary
                                                             , root_index+1, ine, poe-num_elems_right_subtree, poe-1)
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)

        dictionary = {}
        for i in range(n):
            dictionary[inorder[i]] = i

        root = self.build_tree_using_inorder_postorder(inorder, postorder, dictionary, 0, n-1, 0, n-1)
        return root