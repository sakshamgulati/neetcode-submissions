class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(n)}
        for src, dst in edges:
            adj_list[src].append(dst)

        visited = set()
        path = set()
        tp_srt = []

        def dfs(node):
            if node in path:        # back on the current stack → cycle
                return False
            if node in visited:     # already fully finished → safe to skip
                return True
            visited.add(node)
            path.add(node)          # entering the stack
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False    # pass the cycle signal upward
            path.remove(node)       # leaving the stack
            tp_srt.append(node)
            return True

        for i in range(n):
            if not dfs(i):
                return []

        tp_srt.reverse()
        return tp_srt