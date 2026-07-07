class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mystack=[] 
        ans=[0] * len(temperatures)  
        for index,value in enumerate(temperatures): #[30,38,32,36]
            while mystack and value > mystack[-1][1]: #36 > 32
                popped_index,popped_val= mystack.pop() #2,32 
                print(mystack)
                ans[popped_index]= index-popped_index #[1,0,1,0]
            mystack.append((index,value)) #[32,38]
        return ans

