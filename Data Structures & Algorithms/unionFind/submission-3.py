class UnionFind:
    
    def __init__(self, n: int):
        self.par={}
        self.rank={}
        for child in range(n):
            self.par[child]=child #{1:1}
            self.rank[child]=1
        self.counter=n


    def find(self, x: int) -> int:
        # will return the parent , or itself if there is no parent
        if self.par[x]!= x:
            self.par[x]= self.find(self.par[x])
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        #if parents are the same return true, else false
        return self.find(x)==self.find(y)


    def union(self, x: int, y: int) -> bool:
        #find parents
        p1,p2 = self.find(x),self.find(y)
        if p1==p2:
            return False
        else:
            if self.rank[p1]==self.rank[p2]:
                self.par[p1]=p2
                self.rank[p2]+=1
            elif self.rank[p1] > self.rank[p2]:
                self.par[p2]=p1
            else:
                self.par[p1]=p2
            self.counter -=1
            return True
        

    def getNumComponents(self) -> int:
        return self.counter
        

