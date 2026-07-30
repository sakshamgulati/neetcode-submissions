class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        robSum1,robSum2=[0]*len(nums),[0]*len(nums)
        maxrobSum1,maxrobSum2= 0,0
        for i in range(len(nums)-1):
            robSum1[i]= nums[i] if i < 2 else nums[i]+max(robSum1[i-3],robSum1[i-2])
            maxrobSum1 = max(maxrobSum1,robSum1[i])
        for i in range(1,len(nums)):
            robSum2[i]= nums[i] if i < 2 else nums[i]+max(robSum2[i-3],robSum2[i-2])
            maxrobSum2 = max(maxrobSum2,robSum2[i])
        return max(maxrobSum1,maxrobSum2)