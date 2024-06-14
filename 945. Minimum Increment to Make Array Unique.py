class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        count = [0]*(n+max(nums)+1)
        res = 0 

        for i in freq:
            count[i] = freq[i]
        
        for i in range(len(count)):
            if count[i] > 1:
                res += count[i]-1
                count[i+1] = count[i+1] + count[i] - 1
                count[i] = 1
        
        return res
                
        
