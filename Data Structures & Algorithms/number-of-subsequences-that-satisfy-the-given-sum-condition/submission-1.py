class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD= (10**9)+7
        rp=len(nums)-1
        ans=0
        for lp in range(len(nums)):
            while nums[lp]+nums[rp]>target and rp>=lp:
                rp-=1
            if lp <=rp:
                ans += 2**(rp-lp)
                ans %=  MOD
        return ans   
