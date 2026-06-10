class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        ans= 0
        for n in nums:
            count=0
            if n-1 not in numSet:
                i= n
                while i in numSet:
                    count +=1
                    i+=1 
                ans=max(ans,count)
        return ans    