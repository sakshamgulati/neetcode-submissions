class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures) #[1,4,0,0,0]
        stack=[]
        for i,v in enumerate(temperatures): 
                while stack and v > stack[-1][1]:
                    i_index,i_val =stack.pop() #2,30
                    ans[i_index]= i- i_index 
                stack.append([i,v]) 
        return ans


        