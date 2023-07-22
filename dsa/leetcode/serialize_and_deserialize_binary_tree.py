# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return str([])

        queue = deque()
        queue.append(root)
        ans = []

        while len(queue) != 0:
            temp = queue.popleft()
            if temp:
                ans.append(temp.val)
                queue.append(temp.left)
                queue.append(temp.right)
            else :
                ans.append(None)
        return str(ans)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 2:
            return None
        data_list = list(data[1:-1].split(','))

        queue = deque()
        val_str = data_list[0].strip()
        root_val = int(val_str)
        root = TreeNode(root_val)
        queue.append(root)

        i = 1
        while len(queue) != 0:
            parent = queue.popleft()

            val_str = data_list[i].strip()
            if val_str != "None":
                val = int(val_str)
                node = TreeNode(val)
                parent.left = node
                queue.append(node)
            i = i+1

            val_str = data_list[i].strip()
            if val_str != "None":
                val = int(val_str)
                node = TreeNode(val)
                parent.right = node
                queue.append(node)
            i = i+1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))