class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols= len(grid),len(grid[0])
        substack=set()
        islands=0

        def bfs():
            from collections import deque
            q= deque()
            q.append((r,c))
            while q:
                row,col= q.popleft()
                for dr,dc in [[1,0],[0,-1],[-1,0],[0,1]]:
                    newr= row+dr
                    newc=col+dc
                    if newr in range(rows) and newc in range(cols) and grid[newr][newc] =="1" and (newr,newc) not in substack  :
                        q.append((newr,newc))
                        substack.add((newr,newc))
                    

                



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in substack:
                    bfs()
                    islands+=1
        return islands

