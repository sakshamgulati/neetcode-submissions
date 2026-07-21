class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_happiness= 0
        for index in range(len(customers)): #8
            if grumpy[index]==0: 
                base_happiness += customers[index] #1+1+1+7=10
        
        max_gain=0
        for index in range(len(customers)):
            if grumpy[index]==1:
                incremental_gain= 0
                j=0
                while (index+j) < len(customers) and j < minutes:
                    incremental_gain += (grumpy[index+j]*customers[index+j]) 
                    j +=1
                max_gain= max(incremental_gain,max_gain)
        return max_gain + base_happiness



