class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp,rp=0,len(numbers)-1
        while lp < rp:
            if numbers[lp] + numbers[rp] == target:
                return [lp+1,rp+1]
            elif numbers[lp] + numbers[rp] > target:
                rp -=1
            else:
                lp +=1
            
        