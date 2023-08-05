"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        dq = deque()
        dq.append([root])

        while dq:
            level_nodes = dq.pop()
            m = len(level_nodes)
            next_level_nodes = []
            for i in range(m-1):
                if level_nodes[i].left:
                    next_level_nodes.append(level_nodes[i].left)
                if level_nodes[i].right:
                    next_level_nodes.append(level_nodes[i].right)
                level_nodes[i].next = level_nodes[i+1]
            if level_nodes[m-1].left:
                next_level_nodes.append(level_nodes[m-1].left)
            if level_nodes[m-1].right:
                next_level_nodes.append(level_nodes[m-1].right)
            level_nodes[m-1].next = None
            # level_nodes[m-1].next = level_nodes[0].left
            if next_level_nodes:
                dq.append(next_level_nodes)

        temp = root
        while temp:
            print(temp.val,end=" ")
            temp = temp.next

        return root