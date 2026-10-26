class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        import heapq
        adj_list={i:[] for i in range(n)}
        for (u, v), p in zip(edges, succProb):
            adj_list[u].append((v, p))
            adj_list[v].append((u, p))        #hash map for visited 
        visited={}
        maxHeap=[[-1,start_node]] #prob,node - initializing with 1 prob of visiting startnode
        while maxHeap:
            popped_prob, popped_node= heapq.heappop(maxHeap) #-0.5,1
            if popped_node in visited:
                continue
            visited[popped_node]= -1*popped_prob #visited-> [0:1, 1:0.5]
            for child,prob in adj_list[popped_node]: #[[2, 0.5]]
                heapq.heappush(maxHeap,[popped_prob*prob,child]) # [-1*0.5,1],[-1*0.2,2]
        print(visited)
        return visited[end_node] if end_node in visited else 0



