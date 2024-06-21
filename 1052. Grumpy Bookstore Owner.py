class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        right = minutes
        best = cur = sum(grumpy[i]*customers[i] for i in range(minutes))
        while right < len(customers):
            cur -= customers[right - minutes]*grumpy[right - minutes]  
            cur += customers[right]*grumpy[right]  
            best = max(best, cur)
            right += 1
        
        return sum((1 - grumpy[i])*customers[i] for i in range(len(customers))) + best
