class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        cost.append(0)
        runningCost=[0]*len(cost)
        runningCost[0]=cost[0]
        runningCost[1]=cost[1]
        for i in range(2,len(runningCost)):
            runningCost[i]=min(runningCost[i-1],runningCost[i-2])+cost[i]
        return runningCost[-1]
