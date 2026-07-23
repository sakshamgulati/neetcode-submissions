class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lp,rp=0,0
        rsum,ans=0,0
        while rp < len(nums):
            rsum += nums[rp]
            while rp-lp > rsum:
                rsum -= nums[lp]
                lp+=1
            ans= max(ans,rp-lp+1)
            rp+=1
        return ans