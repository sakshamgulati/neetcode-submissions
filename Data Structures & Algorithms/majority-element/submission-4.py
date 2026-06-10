class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counter= dict(Counter(nums))
        top_count= sorted(list(counter.values()),reverse= True)[0]
        for k,v in counter.items():
            if v==top_count:
                return k


        