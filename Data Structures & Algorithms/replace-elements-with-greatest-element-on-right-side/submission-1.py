class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[-1]*len(arr) # [-1,-1,-1,-1,-1,-1]
        for i in range(len(arr)):
            max_num= -1
            for j in range(i+1,len(arr)): 
                max_num= max(max_num,arr[j]) #max(-1,4)               
            ans[i]=max_num
        return ans