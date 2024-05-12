class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def getmax(i,j):

            return max(grid[i][j],grid[i-1][j],grid[i][j-1],grid[i+1][j],grid[i][j+1],
            grid[i-1][j-1],grid[i-1][j+1],grid[i+1][j-1],grid[i+1][j+1])
        
        res = []
        row, col = len(grid), len(grid[0])
        for i in range(1,row-1):
            temp=[]
            for j in range(1,col-1):
                temp.append(getmax(i,j))
            res.append(temp)
        
        return res

        
       
        
