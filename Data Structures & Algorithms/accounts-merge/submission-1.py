class UnionFind:
    def __init__(self,n):
        self.par={}
        self.rank={}
        for i in range(n):
            self.par[i]=i
            self.rank[i]=1
        
    def find(self,x):
        p = x
        while p != self.par[p]:
            p = self.par[p]
        return p

    def union(self,x,y):
        p1,p2= self.find(x), self.find(y)
        if p1==p2:
            return False
        else:
            if self.rank[p1] == self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] +=1
            elif self.rank[p1] > self.rank[p2]:
                self.par[p2]=p1
            else:
                self.par[p1]= p2
            return True



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #step1- email to account conversion 
        
        uf= UnionFind(len(accounts))
        email_to_acc= {}
        for index,account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_acc.keys():
                    email_to_acc[email] =  index
                else:
                    uf.union(email_to_acc[email],index)
        
        #step2- email to account iteration, grouping emails by leader
        from collections import defaultdict
        leader_email_mapping= defaultdict(list)
        for emails,index in email_to_acc.items(): #{0: x@gmail.com, 1:y@gmail.com}
            # if email has no 
            
            leader = uf.find(index)
            leader_email_mapping[leader].append(emails)
            # output - {0: [x@gmail.com, b@gmail.com], 1:[y@gmail.com]}

        #step3- merge names and sorted emails
        # {0: [x@gmail.com, b@gmail.com], 1:[y@gmail.com]}
        # {john:[x@gmail.com, b@gmail.com], angels:[y@gmail.com] }
        res= []
        for index,emails in leader_email_mapping.items():
            name = accounts[index][0]
            emails = sorted(emails)
            res.append([name]+emails)
        return res


        