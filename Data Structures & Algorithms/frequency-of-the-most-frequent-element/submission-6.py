class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,0
        max_count,total=0,0
        while r < len(nums):
            total += nums[r]
            while total + k < nums[r]*(r-l+1):
                total -= nums[l]
                l+=1
            max_count= max(max_count,r-l+1)
            r+=1
        return max_count