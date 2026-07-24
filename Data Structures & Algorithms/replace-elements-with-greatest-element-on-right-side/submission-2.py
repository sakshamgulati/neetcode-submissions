class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight= -1
        for index in range(len(arr)-1,-1,-1):
            temp = arr[index]
            arr[index] = maxRight
            maxRight = max(temp,maxRight)
        return arr
        