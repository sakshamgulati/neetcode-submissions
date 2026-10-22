class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        adj_list={}
        for i in range(1,n+1):
            adj_list[i]=[]
        
        for source,dest,w in times:
            adj_list[source].append([w,dest])
        #min heap instantiated by k
        minHeap=[[0,k]]
        #minimum weight for every node 
        result={}
        while minHeap:
            x=heapq.heappop(minHeap)
            pop_dist, pop_node= x
            if pop_node in result.keys():
                continue
            #add to the results if pop_node doesnt in result
            result[pop_node]=pop_dist
            for dist,node in adj_list[pop_node]:
                heapq.heappush(minHeap,[dist+pop_dist,node])
        
        ans=0
        print(result)
        for node in adj_list:
            if node not in result.keys():
                return -1
        for node in result.keys():
            ans = result[node]
        return ans
        