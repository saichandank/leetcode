# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def helper(root,val):
            if not root:
                return val
            r = helper(root.right,val)
            root.val += r
            l = helper(root.left,root.val)

            return l
        helper(root,0)
        return root
