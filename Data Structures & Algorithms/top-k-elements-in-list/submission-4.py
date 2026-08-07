class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        freq_count= Counter(nums)
        nums=[]
        heapq.heapify(nums)
        for items,count in freq_count.items():
            heapq.heappush(nums,(count,items))
            if len(nums) > k:
                heapq.heappop(nums)
        return [i for c,i in nums]
        