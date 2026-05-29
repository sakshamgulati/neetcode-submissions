class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            rsum=nums[i]
            for j in range(i+1,len(nums)):
                rsum += nums[j]
                if rsum % k ==0:
                    print(rsum)
                    return True
        return False
        