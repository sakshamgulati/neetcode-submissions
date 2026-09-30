class MedianFinder:

    def __init__(self):
        import heapq
        self.maxHeap=[]
        self.minHeap=[]

    def addNum(self, num: int) -> None:
        if len(self.maxHeap)>0:
            if num > -self.maxHeap[0]:
                heapq.heappush(self.minHeap,num)
            else:
                heapq.heappush(self.maxHeap,-num)
        else:
            heapq.heappush(self.maxHeap,-num)
        #rebalance after every iteration
        #compare the lengths of two heaps
        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
            else:
                heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if not self.maxHeap:
            return None
        if len(self.maxHeap)==len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        else:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            else:
                return self.minHeap[0]
        
        