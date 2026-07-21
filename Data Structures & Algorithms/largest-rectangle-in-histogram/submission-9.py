class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mystack=[]
        ans= 0 
        for index,items in enumerate(heights):
                while mystack and items < mystack[-1][1]:
                    popped_index,popped_val = mystack.pop()
                    right = index
                    left = mystack[-1][0] if mystack else -1
                    ans= max(ans,popped_val* (right -left-1))
                mystack.append((index,items))
        print(mystack)
        for pos, (idx, value) in enumerate(mystack):
            right = len(heights)
            left = mystack[pos - 1][0] if pos > 0 else -1
            ans = max(ans, value * (right - left - 1))
        return ans
