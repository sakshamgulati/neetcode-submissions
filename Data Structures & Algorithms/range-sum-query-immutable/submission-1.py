class NumArray:

    def __init__(self, nums: List[int]):
        self.nums= nums
        self.prefix=[]
        rsum=0
        for n in self.nums:
            rsum +=n
            self.prefix.append(rsum)



    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left-1] if left > 0 else 0
        return rightSum-leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)