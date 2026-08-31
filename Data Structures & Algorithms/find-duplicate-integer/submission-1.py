class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm={}
        for n in nums:
            hm[n]= hm.get(n,0)+1
            if hm[n]>1:
                return n
        
            