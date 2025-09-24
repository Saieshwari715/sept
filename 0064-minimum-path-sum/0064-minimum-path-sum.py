class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        sum = 0
        l = 0
        r = len(grid[0]) - 1 
        b = len(grid) - 1    
        for i in range(l+1, r+1):
            grid[0][i] += grid[0][i-1]
        for i in range(l+1, b+1):
            grid[i][0] += grid[i-1][0]
        for i in range(1, b+1):
            for j in range(1, r+1):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        sum = grid[b][r]
        return sum