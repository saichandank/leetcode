class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])

        for r in range(row):
            if grid[r][0] == 0:
                for c in range(col):
                    grid[r][c] ^= 1
        
        cz =[0]*col
        for r in range(row): 
            for c in range(col):
                if grid[r][c] == 0:
                    cz[c]+=1
        
        for c in range(col):
            if cz[c] >= (row/2):
                
                for r in range(row):
                    grid[r][c] ^= 1
        
        res = 0
        for r in range(row):
            rval = 0
            for c in range(col):
                rval = rval + 2**(col-1-c) * grid[r][c]
            res+=rval
        
        return res


        

