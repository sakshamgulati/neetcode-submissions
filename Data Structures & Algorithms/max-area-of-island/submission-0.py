class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols= len(grid),len(grid[0])
        substack=set()
        max_area=0
        if not grid:
            return max_area
        
        def bfs(row, col):
            from collections import deque
            q= deque()
            q.append([row,col])
            substack.add((row,col))
            area = 1
            while q:
                r,c = q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    new_r, new_c= r+dr, c+dc
                    if new_r in range(rows) and new_c in range(cols) and (new_r,new_c) not in substack and grid[new_r][new_c]==1:
                        q.append([new_r,new_c])
                        substack.add((new_r,new_c))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in substack:
                    max_area= max(max_area, bfs(r, c))
        return max_area