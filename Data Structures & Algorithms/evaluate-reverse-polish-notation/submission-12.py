class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #continue to add elements in the stack 
        # when the len of the stack > 2, act on the element
        # push the new element back
        
        stack= []
        for items in tokens:
            if items in ["+","-","*","/"]: 
                b= stack.pop() #4
                a= stack.pop() #9
                if items == "+":
                    output= a+b 
                elif items=="*":
                    output = a*b 
                elif items =="/":
                    output = int(a/b)
                elif items=="-":
                    output = a-b #9-4
                stack.append(output) #[9]
            else:
                stack.append(int(items)) #[9,4]
        return stack[-1]
