class MinStack:

    def __init__(self):
        self.stack=[]
        self.minbyStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minbyStack:
            self.minbyStack.append(val)
        else:
            minVal = min(val,self.minbyStack[-1])
            self.minbyStack.append(minVal)


    
    def pop(self) -> None:
        
        self.minbyStack.pop()

        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minbyStack[-1]

        
