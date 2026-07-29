class Solution:
    def rob(self, nums: List[int]) -> int:
        sumRob=[0]*len(nums)
        i=0
        maxReturn=0
        while i < len(nums):
            sumRob[i] += nums[i] if i < 2 else max(sumRob[i-2],sumRob[i-3])+nums[i]
            maxReturn = max(sumRob[i],maxReturn)
            i+=1
        print(sumRob)
        return maxReturn
        
