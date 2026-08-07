class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans= 0
        start,end= 0,k-1 #3
        sumT= k* threshold # 16
        rsum=0
        for i in range(end+1):
            rsum += arr[i] #16
        print(rsum)
        while end < len(arr)-1:
            if rsum >= sumT:
                ans+=1
            end+=1
            rsum += arr[end]-arr[start]
            start+=1
        print(arr[start:end+1],rsum)
        if rsum >= sumT:
            ans+=1
        return ans