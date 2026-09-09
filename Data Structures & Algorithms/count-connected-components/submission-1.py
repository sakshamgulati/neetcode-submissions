class Unionfind:
    def __init__(self,n):
        self.par={}
        self.rank={}
        for i in range(n):
            self.par[i]=i
            self.rank[i]=1
        
    def find(self,x):
        p = x
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self,x,y):
        p1,p2= self.find(x),self.find(y)
        if p1 == p2:
            return False
        else:
            if self.rank[p1] == self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] +=1
            elif self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
            else:
                self.par[p1] = p2
            return True
        


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = Unionfind(n)
        connected = 0 
        for e in edges:
            x,y = e[0],e[1]
            connected += uf.union(x,y)
        return n - connected