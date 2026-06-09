class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j=0,0
        ans=0
        while j < len(nums):
            if nums[j] != val:
                nums[i]=nums[j]
                i+=1
                ans +=1
            j+=1
        return ans
        