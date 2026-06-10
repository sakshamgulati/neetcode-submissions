class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import heapq
        
        myCounter= {}
        for items in nums:
            if items not in myCounter:
                myCounter[items]=1
            else:
                myCounter[items]+=1
        countTracker = [(-v,k) for k,v in myCounter.items()]
        heapq.heapify(countTracker)
        print(countTracker)
        return countTracker[0][1]

        