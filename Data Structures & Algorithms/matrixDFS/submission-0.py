class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        count=0
        substack= set()

        def dfs(grid,row,col):
            if row >= len(grid) or col >=len(grid[0]) or grid[row][col]==1 or row <0 or col < 0 or (row,col) in substack:
                return 0
            if row==len(grid)-1 and col==len(grid[0])-1:
                return 1
            substack.add((row,col))
            #choices
            count = dfs(grid,row+1,col) + dfs(grid,row-1,col) + dfs(grid,row,col+1) + dfs(grid,row,col-1)
            
            #  pop 
            substack.remove((row,col))
            return count
        return dfs(grid,0,0)

        
            