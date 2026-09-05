class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.rank = {i: 1 for i in range(1, n + 1)}
        self.parent = {i: i for i in range(1, n + 1)}

        for a, b in edges:
            result = self.union(a, b)
            if result is not None:
                return result
        return []

    def findParent(self, x):
        p = self.parent[x]
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, a, b):
        p1, p2 = self.findParent(a), self.findParent(b)
        if p1 == p2:
            return [a, b]
        if self.rank[p1] == self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
        return None