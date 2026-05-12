class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        row,col=0,0
        if grid[row][col]==1:
            return -1
        else:
            queue=deque([[row,col]])

        distance=0
        substack=set()
        substack.add((0,0))
        while queue:
            len_q= len(queue)
            for i in range(len_q):
                # pop
                r,c= queue.popleft()
                
                # check if its destination
                if r==len(grid)-1 and c==len(grid[0])-1:
                    if grid[r][c]==1:
                        return -1
                    else:
                        return distance
                # check if neighbours are valid
                
                for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >=len(grid) or nc >= len(grid[0]) or grid[nr][nc]==1 or grid[nr][nc]==1 or (nr,nc) in substack:
                        continue
                    else:
                        queue.append((nr,nc))
                        substack.add((nr,nc))

                
            distance+=1
        return -1