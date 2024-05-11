class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        found = set()
        n = len(nums)
        for i in range(n):
            j = i+1
            k = n-1
            target = -nums[i]
            while j < k:
                su = nums[j]+nums[k]
                if su == target and (nums[i],nums[j],nums[k]) not in found:
                    res.append([nums[i],nums[j],nums[k]])
                    found.add((nums[i],nums[j],nums[k]))
                if  su > target:
                    k -= 1
                else :
                    j += 1
                    
        return res
                
                
        
