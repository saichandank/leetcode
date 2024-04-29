class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        curr=0

        for i in nums:
            curr ^= i
        
        flip = 0
        while curr or k :
            x = curr & 1
            y = k & 1

            if x!=y :
                flip+=1
            
            curr = curr >> 1
            k = k >> 1
        
        return flip

        
