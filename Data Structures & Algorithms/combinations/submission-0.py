class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, temp = [], []
        def dfs(i):
            
            if len(temp) == k:
                ans.append(temp.copy())
                return
            if i > n:
                return
            #choice 1 - take the next element
            temp.append(i)
            dfs(i+1)
            temp.pop()

            #choice 2- dont 
            dfs(i+1)
        dfs(1)
        return ans