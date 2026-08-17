class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for n in range(len(numbers)): #[1,2,3,4]
            if target - numbers[n] in hashmap.keys(): #3-2 ->1 
                return [hashmap[target-numbers[n]]+1,n+1]
            else:
                hashmap[numbers[n]]=n #[1: 0]
        return -1
        
        