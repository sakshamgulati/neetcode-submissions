class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        def dfs(node,adj_list,tp_srt):
            if node in path:
                return False
            if node in visited:
                return True
            visited.add(node)
            path.add(node)
            for neighbor in adj_list[node]:
                if not dfs(neighbor,adj_list,tp_srt):
                    return False
            tp_srt.append(node)
            path.remove(node)
            return True

        adj_list={}
        for i in range(n):
            adj_list[i]=[]
        for src,dst in edges:
            adj_list[src].append(dst)

        visited=set()
        tp_srt=[]
        path= set()

        for i in range(n):
            if not dfs(i,adj_list,tp_srt):
                return []
        tp_srt.reverse()
        return tp_srt
