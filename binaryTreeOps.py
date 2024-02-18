from itertools import chain
from queue import Queue
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class TreeOps:
    def __init__(self) -> None:
        pass

    def BFS(self, root):
        if root is None:
            return
        q = Queue()
        visited = {}
        q.put(root) 
        while not q.empty():
            currentNode = q.get()
            visited[currentNode.val] = True
            if currentNode.left is not None:
                q.put(currentNode.left)
            if currentNode.right is not None:
                q.put(currentNode.right)

        

    def recursiveDFS(self, root):
        if root is None:
            return
        leftval = self.recursiveDFS(root.left)
        rightval = self.recursiveDFS(root.right)
        return list(chain([root.val, leftval, rightval]))
        

    def DFS(self, root):
        visited = {}
        stack = []
        stack.append(root)
        if root is None:
            return
        while stack:
            current_node = stack.pop()
            visited[current_node.val] = True
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        print('')

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')

node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.right = node_f

treeObj = TreeOps()
travsered_nodes = treeObj.BFS(node_a)
print(travsered_nodes)
"""
        a
       / \
      b   c
     /\   \
    d e    f
"""