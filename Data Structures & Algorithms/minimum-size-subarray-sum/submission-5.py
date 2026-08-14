class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp,rp=0,0
        ans,rsum=float('inf'),0
        while rp < len(nums):
            rsum+= nums[rp]
            while rsum >= target:
                ans = min(rp-lp+1,ans)
                rsum -= nums[lp]
                lp+=1
            rp+=1 

        return ans if ans != float('inf') else 0
        