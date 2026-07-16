class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        cumsum=0
        for i in range(k): # 3
            cumsum += arr[i]
        if cumsum >= (threshold*k):
            count+=1 
        for i in range(k,len(arr)):
            cumsum += arr[i]  - arr[i-k]
            if cumsum >= (threshold*k): # 10 > 15
                count+=1
        return count