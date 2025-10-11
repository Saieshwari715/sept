class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res=0
        fresh=0
        rows,cols=len(grid),len(grid[0])
        q=deque()
        direc=[(0,1),(1,0),(-1,0),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==2):
                    q.append((r,c,0))
                if(grid[r][c]==1):
                    fresh+=1
        while q:
            row,col,g=q.popleft()
            for dr,dc in direc:
                r,c=row+dr,col+dc
                if 0<=r<rows and 0<=c<cols and grid[r][c]==1:
                    grid[r][c]=2
                    fresh-=1
                    q.append((r,c,g+1))
                    res=max(res,g+1)
        if fresh==0:
            return res
        else:
            return -1

        