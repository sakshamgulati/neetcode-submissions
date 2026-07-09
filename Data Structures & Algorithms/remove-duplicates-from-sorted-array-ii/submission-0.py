class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter={}
        for items in nums:
            counter[items]=1+ counter.get(items,0)
        # { 1: 3, 2:2, 3:1}
        rp=0
        for n in counter.keys(): #[1,2,3]
            for _ in range(min(2,counter[n])): #3
                nums[rp] = n #[1,1,2,2,3]
                rp+=1 # 5
        return rp
        