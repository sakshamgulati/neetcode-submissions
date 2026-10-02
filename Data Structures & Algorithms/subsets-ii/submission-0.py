class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans,subset=[],[]
        nums= sorted(nums)
        def dfs(i):
            if i >= len(nums):
                subset.append(ans.copy())
                return
            
            ans.append(nums[i])
            dfs(i+1)
            ans.pop()

            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return subset 

        