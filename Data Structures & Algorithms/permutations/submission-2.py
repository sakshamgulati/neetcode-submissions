class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        substack=[]

        def dfs():
            
            if len(substack.copy())==len(nums):
                ans.append(substack.copy())
                return

            for items in nums:
                if items not in substack:
                    substack.append(items)
                    dfs()
                    substack.pop()
            
        dfs()
        return ans