class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # instantiate a list that has its index-nodes listed
        nodes= len(edges) # [[1,2],[1,3],[3,4],[2,4]]
        parent = list(range(nodes+1)) # index = [0,1,2,3,4]

        def find(a):
            if parent[a]==a:
                return a
            return find(parent[a])

        for a,b in edges:
            #check parents 
            # if different then its good
            if find(a)!= find(b):
                parent[find(b)] = find(a)
            else:
                return [a,b]
        


            

