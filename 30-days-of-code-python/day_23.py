import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, node, depth = 0, levels = None):
        if not depth:
            levels = defaultdict(list)
            levels[depth].append(node.data)

        nodes = [n for n in [node.left, node.right] if n != None]

        for n in nodes:
            levels[depth+1].append(n.data)
            self.levelOrder(n, depth+1, levels)
        
        if not depth:
            result = [str(level) for i in range(len(levels)) for level in levels[i]]
            print(" ".join(result))

from collections import defaultdict  # Cannot import on top because of locked stub code

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)