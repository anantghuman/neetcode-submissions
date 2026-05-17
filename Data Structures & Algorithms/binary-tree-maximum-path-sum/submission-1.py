# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        hm = {}
        def recurse(node):
            if node is None:
                return 0
            l, r = recurse(node.left), recurse(node.right)
            hm[node] = node.val + max(l, 0) + max(r, 0)
            return max(node.val + l, node.val + r, node.val)


        recurse(root)
        return max(hm.values())
        