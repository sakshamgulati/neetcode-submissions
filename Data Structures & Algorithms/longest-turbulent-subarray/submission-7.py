class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        temp= [0]*len(arr)
        for rp in range(1,len(arr)):
            if arr[rp] > arr[rp-1]:
                temp[rp]=1
            elif arr[rp] < arr[rp-1]:
                temp[rp]=-1
        lp,ans=0,0
        print(temp)
        for rp in range(1,len(temp)): #[0,1,-1,-1,0,1,-1,1]
            if temp[rp]==0:
                lp=rp
            elif temp[rp-1]==temp[rp]:
                lp= rp-1
            ans= max(ans,rp-lp+1)
        return ans if len(temp)> 1 else  1

        