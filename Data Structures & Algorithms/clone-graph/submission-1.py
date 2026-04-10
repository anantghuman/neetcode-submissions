"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hm = {}
        visited = set()

        def clone(node):
            if node in visited:
                return hm[node]
            visited.add(node)
            c = None
            if node in hm:
                c = hm[node]
            else:
                c = Node()
                c.val = node.val
                hm[node] = c
            for neighbor in node.neighbors:
                c.neighbors.append(clone(neighbor))
            return c
        if node is None:
            return None
        return clone(node)
        
        