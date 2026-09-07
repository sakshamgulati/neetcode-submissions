from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        N = len(accounts)
        
        # --- STEP 1: BUILD THE GRAPH ---
        adj = defaultdict(list)
        for i in range(N):
            emails = accounts[i][1:]
            for j in range(i + 1, N):
                for email in emails:
                    if email in accounts[j][1:]:
                        adj[i].append(j)
                        adj[j].append(i)
                        break

        # --- STEP 2: DFS TRAVERSAL ---
        visited = set()
        result = []

        def dfs(node: int, merged_emails: set):
            visited.add(node)
            
            # Add emails from the current account
            for email in accounts[node][1:]:
                merged_emails.add(email)

            # Recursively visit all connected accounts in the chain
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, merged_emails)

        # --- STEP 3: PROCESS ALL UNVISITED COMPONENTS ---
        for i in range(N):
            if i not in visited:
                name = accounts[i][0]
                merged_emails = set()
                
                dfs(i, merged_emails)
                
                result.append([name] + sorted(merged_emails))

        return result