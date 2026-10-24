class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # you need a min heap, pop out each time
        # its a 2d grid so yu need directions [1,0],[-1,0] and such
        # anytime you go out of bounds you continue
        # other time you add the max(value, current grid ) to the min heap
        # when you reach the n= len(grid)-1 you return the visited max
        visited=[]
        n= len(grid)
        minHeap= [[grid[0][0],0,0]] #[value, x,y]
        directions= [[1,0],[0,1],[-1,0],[0,-1]] #right,up,left,down
        while minHeap:
            pop_value,x,y= heapq.heappop(minHeap)
            if x==n-1 and y==n-1:
                return pop_value
            for dr,dy in directions:
                new_x= x+dr
                new_y= y+dy
                if (new_x < 0 or new_y >=n or [new_x,new_y] in visited or new_x >=n or new_y <0) :
                    continue
                visited.append([new_x,new_y])
                heapq.heappush(minHeap,[max(pop_value,grid[new_x][new_y]),new_x,new_y])




