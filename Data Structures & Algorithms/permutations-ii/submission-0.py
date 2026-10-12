class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans,subset=[],[]
        def dfs():
            if len(subset)==len(nums):
                ans.append(subset.copy())
                return
            
            for index,val in enumerate(nums):
                if (index,val) not in subset:
                    subset.append((index,val))
                    dfs()

                    subset.pop()
        dfs()
        
        res= []
        for vals in ans:
            test=[]
            for v in vals:
                test.append(v[1])
            
            if test not in res:
                res.append(test)
                
        return res
            