class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_array=[1]*len(nums)
        backward_array=[1]*len(nums)
        for i in range(1,len(nums)):
            forward_array[i]= nums[i-1]*forward_array[i-1]
        for i in range(len(nums)-2,-1,-1):
            backward_array[i]=backward_array[i+1]*nums[i+1] 
        return [forward_array[i]*backward_array[i] for i in range(len(nums))]                   