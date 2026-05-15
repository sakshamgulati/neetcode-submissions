class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)< 2:
            try:
                return nums[0]
            except IndexError:
                return 0

        runningTotal= [0]*len(nums)
        runningTotal[0] = nums[0]
        runningTotal[1] = nums[1]
        for i in range(2,len(nums)):
            runningTotal[i]= max(runningTotal[i-2],runningTotal[i-3])+ nums[i]
        return max(runningTotal)
        
