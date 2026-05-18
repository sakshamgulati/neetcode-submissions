class Solution:
    
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1:
            return nums[0]
        def circular_rob(nums):
            r1,r2=0,0
            for i in range(len(nums)):
                temp = max(r1+nums[i],r2)
                r1= r2
                r2= temp
            
            return r2
    
        return max(circular_rob(nums[:n-1]),circular_rob(nums[1:]))
