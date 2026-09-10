class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums) #2,20,4,10,3,5
        ans= 0
        for n in numSet: #2
            if n-1 not in numSet: 
                temp = n #2
                k = 1 #1
                while temp in numSet: #6
                    ans = max(ans,k) 
                    k+=1 #
                    temp+=1 #
        return ans
        