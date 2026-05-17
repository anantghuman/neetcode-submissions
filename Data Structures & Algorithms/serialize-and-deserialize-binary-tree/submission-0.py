# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = []
        q = deque()
        q.append(root)
        while q:
            s = q.popleft()
            if s is None:
                string.append("None")
            else:
                string.append(str(s.val))
                q.append(s.left)
                q.append(s.right)

        return ','.join(string)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = deque(data.split(','))
        q = deque()
        head = None if data[0] == "None" else TreeNode(data[0])
        data.popleft()
        q.append(head)
        while data and q:
            t = q.popleft()
            if data[0] != "None" :
                t.left = TreeNode(data.popleft())
                q.append(t.left)
            else:
                data.popleft()
            if data[0] != "None":
                t.right = TreeNode(data.popleft())
                q.append(t.right)
            else:
                data.popleft()
        return head

