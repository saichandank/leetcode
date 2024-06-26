class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = float('-inf')
        
        i = 0
        j = len(height)-1
        
        while i < j:
            res = max(res, min(height[i],height[j])*(j-i))
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return res
                
        
