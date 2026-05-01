"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}

        t = head
        while t is not None:
            if t not in hm:
                hm[t] = Node(t.val)
            if t.next and t.next not in hm:
                hm[t.next] = Node(t.next.val)
            hm[t].next =  hm[t.next] if t.next else None
            if t.random and t.random not in hm:
                hm[t.random] = Node(t.random.val)
            hm[t].random =  hm[t.random] if t.random else None
            t = t.next
        return hm[head] if head else None