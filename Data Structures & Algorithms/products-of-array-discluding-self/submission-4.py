class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[2,4,6]
        #pre= [1,1,1]
        #suf= [1,1,1]
        pre= [1]*len(nums)
        suf= [1]*len(nums)
        rsum=1
        for i in range(len(nums)):
            pre[i]=rsum
            rsum= rsum * nums[i]

        lsum=1
        for j in range(len(nums)-1,-1,-1):
            suf[j]=lsum
            lsum= lsum * nums[j]
        ans=[]
        for k in range(len(nums)):
            ans.append(pre[k] * suf[k])
        return ans

