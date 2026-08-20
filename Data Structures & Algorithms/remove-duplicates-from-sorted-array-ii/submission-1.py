class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp,rp=0,0
        hm={}
        while rp < len(nums):
            #if counter > 3 then do not swap
            hm[nums[rp]] = hm.get(nums[rp],0)+1
            # re-insert
            nums[lp]= nums[rp]
            print(f"new value at index:{lp} is {nums[rp]}", hm)
            if hm[nums[rp]]<=2:
                lp+=1
            rp +=1
        return lp