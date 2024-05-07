# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def helper(node):

            if not node:
                return 0
            carry = helper(node.next)
            curr_val = (node.val * 2) + carry
            node.val = curr_val % 10
            return 1 if curr_val >= 10 else 0

            
        
        carry = helper(head)
        if carry :
            node = ListNode(carry)
            node.next = head
            return node
        return head


        
