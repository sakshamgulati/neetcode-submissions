class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            curr = nums[i]
            prior= nums[i-1]
            if (curr % 2 ==0 and prior % 2 ==0) or (curr % 2 !=0 and prior % 2 !=0):
                return False
        return True

