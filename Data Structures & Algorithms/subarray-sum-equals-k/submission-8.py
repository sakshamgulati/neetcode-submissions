class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum={0:1} #prefixsum : count
        rsum=0
        ans=0
        for n in nums:
            rsum +=n
            if (rsum-k) in prefixSum:
                ans = ans + prefixSum[(rsum-k)]
            prefixSum[rsum] = prefixSum.get(rsum,0)+1
        return ans

