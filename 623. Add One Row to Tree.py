# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        head=root
        stack = collections.deque()
        stack.append((root,1))

        if depth == 1:
            temp=TreeNode(val)
            temp.left=root
            return temp

        while stack:
            root,curr_depth = stack.popleft()

            if curr_depth == depth-1:
                if root.left:
                    temp=TreeNode(val)
                    temp.left=root.left
                    root.left=temp
                else:
                    temp=TreeNode(val)
                    root.left=temp
                if root.right:
                    temp=TreeNode(val)
                    temp.right=root.right
                    root.right=temp
                else:
                    temp=TreeNode(val)
                    root.right=temp

            if curr_depth>=depth:
                return head

            if root.left:
                stack.append((root.left,curr_depth+1))
            if root.right:
                stack.append((root.right,curr_depth+1))
        
        return head
        


        
