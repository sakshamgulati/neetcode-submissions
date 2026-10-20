class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #create adj list - [1,10]
        adj={}
        for items in range(n):
            adj[items]=[]
        
        for source,destination,distance in edges:
            if adj[source]==[]:
                adj[source]=[[destination,distance]]
            else:
                adj[source].append([destination,distance])
        
        # stores the final answer and the cities i already visited
        smallest={}
        import heapq
        # compares the city with itself
        minHeap=[[0,src]]
        heapq.heapify(minHeap)
        while minHeap:
            #pop from the min heap
            pop_distance,pop_city = heapq.heappop(minHeap)
            if pop_city in smallest:
                continue
            
            smallest[pop_city]=pop_distance
            for city,dist in adj[pop_city]:
                heapq.heappush(minHeap,[dist+pop_distance,city])

        for key in range(n):
            if key not in smallest:
                smallest[key]=-1
        return smallest