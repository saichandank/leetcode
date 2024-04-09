class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        idx = k
        count = 0
        while tickets:
            for i in range(len(tickets)):
                if tickets[i]:
                    if i == idx and tickets[i]==1:
                        return count+1
                    else:
                        tickets[i]-=1
                        count+=1

