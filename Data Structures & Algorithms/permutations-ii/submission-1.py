class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans,perm=[],[]
        counter={n:0 for n in nums}
        for n in nums:
            counter[n] +=1
        
        def dfs():
            if len(perm)==len(nums):
                ans.append(perm.copy())
                return
            
            for n in counter:
                if counter[n]>0:
                    perm.append(n)
                    counter[n] -=1
                    dfs()

                    counter[n]+=1
                    perm.pop()
        dfs()
        return ans

