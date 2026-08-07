class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        lp,rp=0,k-1
        ans = nums[rp]-nums[lp]
        while rp < len(nums):
            ans= min(ans,nums[rp] - nums[lp])
            rp+=1
            lp+=1
        return ans

       
        
        