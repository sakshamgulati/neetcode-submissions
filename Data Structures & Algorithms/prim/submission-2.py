class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj_list={}
        for i in range(n):
            adj_list[i]=[]

        for src,dst,wei in edges:
            adj_list[src].append([wei,dst])
            adj_list[dst].append([wei,src])
        
        visited=set()
        #instantiating by a random node #0 
        minHeap=[[0,0]] #weight, dst
        mst=0
        while minHeap:
            pop_wei, pop_src= heapq.heappop(minHeap)
            if len(visited) == n:
                return mst
            if pop_src in visited:
                continue
            mst += pop_wei
            visited.add(pop_src)
            for wei,nghbor in adj_list[pop_src]:
                heapq.heappush(minHeap,[wei,nghbor])
        return -1
            

         
        