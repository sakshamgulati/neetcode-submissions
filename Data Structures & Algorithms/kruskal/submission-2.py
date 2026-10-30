class UnionFind:
    def __init__(self,n):
        self.rank={}
        self.par={}
        for i in range(n):
            self.par[i]=i
            self.rank[i]=1
        self.components = n
    
    def find(self,x):
        if self.par[x]!=x:
            self.par[x]= self.find(self.par[x])
        return self.par[x]
    
    def isSameComponent(self,x,y):
        return self.find(x)==self.find(y)
    
    def union(self,x,y):
        if self.isSameComponent(x,y):
            return False
        else:
            par_x = self.find(x)
            par_y= self.find(y)
            if self.rank[par_x]==self.rank[par_y]:
                self.par[par_x]= par_y
                self.rank[par_y] +=1
            elif self.rank[par_x] > self.rank[par_y]:
                self.par[par_y]=par_x
            else:
                self.par[par_x]=par_y
            self.components -=1
            return True

    def getNumComponents(self) -> int:
        return self.components

class Solution:

    
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        import heapq
        minHeap=[]
        for src,dest,wei in edges:
            heapq.heappush(minHeap,[wei,src,dest])
        mst=[]
        unionfind= UnionFind(n)
        ans=0
        while minHeap and len(mst)< n-1:
            pop_wei, pop_src,pop_dst= heapq.heappop(minHeap)
            if not unionfind.union(pop_src,pop_dst):
                continue
            mst.append([pop_src,pop_dst])
            ans += pop_wei
        return ans if len(mst)==n-1 else -1
            