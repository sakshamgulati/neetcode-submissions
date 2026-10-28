class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list={}
        n= len(points)
        for x,y in points:
            adj_list[(x,y)]=[]
        # adj_list-> [[0,0]:[],[2,2]:[],[3,3]:[]]
        for a,b in adj_list.keys():
            for x,y in points:
                if x==a and y==b:
                    continue
                else:
                    adj_list[(a,b)].append([(abs(x-a)+abs(b-y)),x,y])
        #minheap distance,x,y
        minHeap=[[0,points[0][0],points[0][1]]]
        #store items vistied 
        visited= []
        mst=0
        while minHeap:
            pop_dis,pop_x,pop_y= heapq.heappop(minHeap)
            if len(visited)==n:
                return mst 
            if [pop_x,pop_y] in visited:
                continue
            mst += pop_dis
            visited.append([pop_x,pop_y])
            for dist,x,y in adj_list[(pop_x,pop_y)]:
                heapq.heappush(minHeap,[dist,x,y])
        return mst
