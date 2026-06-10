class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output=[intervals[0]]
        
        #need to sort them
        intervals= sorted(intervals, key= lambda x:x[0])
        output=[intervals[0]]
        i=1
        while i < len(intervals):
            laststart,lastend= output[-1][0],output[-1][1]
            start,end= intervals[i][0],intervals[i][1]
            if lastend >= start:
                newstart= min(laststart,start)
                newend= max(lastend,end)
                output[-1][0]=newstart
                output[-1][1]=newend
            else:
                output.append([start,end])
            i+=1
        return output
                



        




