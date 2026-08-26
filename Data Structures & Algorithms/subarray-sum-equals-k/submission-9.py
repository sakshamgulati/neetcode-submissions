class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        rsum=0
        ans=0
        for n in nums:
            rsum +=n #4
            if (rsum - k) in prefixSum: #2
                ans+= prefixSum[(rsum - k)]
            prefixSum[rsum]= prefixSum.get(rsum,0)+1 #{2:2,0:1,1:1,}
        return ans


        
        

