class UnionFind:
    
    def __init__(self, n: int):
        self.par={}
        self.rank={}
        self.counter= n
        for child in range(n):
            self.par[child]=child
            self.rank[child]=0


    def find(self, x: int) -> int:
        # will return the parent , or itself if there is no parent
        parent = self.par.get(x) # {2:2}
        while parent!= self.par.get(parent):
            parent = self.par.get(parent)
        return parent
        

    def isSameComponent(self, x: int, y: int) -> bool:
        #if parents are the same return true, else false
        return self.find(x)==self.find(y)


    def union(self, x: int, y: int) -> bool:
        #find parents
        p1,p2= self.find(x), self.find(y)
        if p1==p2:
            return False
        else:
            
            # rank 1 > rank 0, join rank1 under rank0
            if self.rank[p1] > self.rank[p2]:
                # p2 becomes a child of p1
                self.par[p2]= p1
                
            elif self.rank[p1] == self.rank[p2]:
                self.par[p2]=p1
                self.rank[p1] +=1
                
            else:
                self.par[p1]=p2
            self.counter -=1

            return True
        

    def getNumComponents(self) -> int:
        return self.counter
        

