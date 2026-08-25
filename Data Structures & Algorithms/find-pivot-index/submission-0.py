class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=[0]*len(nums)
        right_sum=[0]*len(nums)
        rsum=0
        for i in range(1,len(nums)):
            rsum = nums[i-1]+rsum
            left_sum[i]= rsum
        rsum=0
        for i in range(len(nums)-2,-1,-1):
            rsum = nums[i+1] + rsum
            right_sum[i] = rsum
        ans = -1
        for index in range(len(left_sum)):
            if left_sum[index]==right_sum[index]:
                return index
        return ans
            