class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp,rp=0,0
        ans,rsum=len(nums),0
        while rp < len(nums):
            while rsum >= target:
                ans = min(rp-lp,ans)
                rsum -= nums[lp]
                lp+=1
            rsum+= nums[rp]
            rp+=1 
        while rsum >= target:
            ans = min(rp-lp,ans)
            rsum -= nums[lp]
            lp+=1
        return ans if target <= sum(nums) else 0
        