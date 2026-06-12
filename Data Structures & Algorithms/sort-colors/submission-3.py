class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sortMap= {}
        for items in nums:
            sortMap[items] = sortMap.get(items,0)+1
        i=0
        for col in [0,1,2]: #2
            if col in sortMap:
                for _ in range(sortMap[col]):
                    nums[i]=col 
                    i+=1 #
        return nums
