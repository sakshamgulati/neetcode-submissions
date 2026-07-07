class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        import heapq
        if len(hand)%groupSize != 0: return False
        # dictionary counter
        counter = {}
        for n in hand:
            counter[n] = 1 + counter.get(n,0) #{1: 1, 2: 1 , 3: 2, 4: 2, 5: 1}
        #min heap to track lowest element
        minH= list(counter.keys())
        heapq.heapify(minH) 

        while minH:
            first= minH[0] #1
            for i in range(first, first+groupSize): #range(1,5)
                if i not in counter:
                    return False
                counter[i] -=1 #{1: 0, 2: 0 , 3: 1, 4: 1, 5: 1}
                if counter[i]==0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        
