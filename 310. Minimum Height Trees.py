from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list=[ [] for _ in range(n)]

        if n < 2:
            return [ i for i in range(n)]

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)


        
        leaves=[]
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)

        remaining=n
        while remaining > 2:
            remaining -= len(leaves)
            temp = []
            while leaves:
                leaf = leaves.pop()

                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)

                if len(adj_list[neighbor])==1:
                    temp.append(neighbor)
            
            leaves = temp
        
        return leaves

