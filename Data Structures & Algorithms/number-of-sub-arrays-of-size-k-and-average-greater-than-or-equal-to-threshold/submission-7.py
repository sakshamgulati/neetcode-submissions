class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        rsum=0
        for _ in range(k):
            rsum+= arr[_]
        ans=0
        start,end= 0,k-1
        thresholdSum= threshold * k
        while end < len(arr):
            if rsum >= thresholdSum:
                ans +=1
            end+=1
            rsum = rsum + arr[end] - arr[start] if end < len(arr) else rsum
            start+=1            
        return ans
         