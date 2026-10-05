class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans,temp =[],[]
        def dfs(i):
            if i >= len(nums):
                return 
            if sum(temp.copy()) == target:
                ans.append(temp.copy())
                return
            if sum(temp.copy()) > target:
                return

            temp.append(nums[i])
            dfs(i)
            temp.pop()

            dfs(i+1)
        dfs(0)
        return ans 