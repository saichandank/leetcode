import heapq
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happy = [-i for i in happiness]
        heapq.heapify(happy)
        count = 0
        value = 0
        while count != k :
            temp = (heapq.heappop(happy) * -1) - count
            if temp <=0 :
                return value
            value += temp
            count += 1
        
        return value
        


        
