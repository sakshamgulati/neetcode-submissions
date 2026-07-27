class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myhash={}
        for index,val in enumerate(nums):
            if val not in myhash.keys():
                myhash[val] = index
            else:
                if index - myhash[val] <= k:
                    return True
                else:
                    myhash[val]=index
        return False
            