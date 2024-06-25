class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        flips = 0
        for i in range(n):

            if i-k >= 0 and nums[i-k] == 2:
                flips -= 1
            
            if (nums[i]+flips) % 2 == 0:
                if i + k > n:
                    return -1
                nums[i] = 2
                count += 1
                flips += 1
        return count
        
