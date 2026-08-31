class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.Cmin = 999999999999999999999999999999999999999999999999999999999999999999999999
        

    def push(self, val: int) -> None:
        self.Cmin = min(self.Cmin, val)
        self.minstack.append(self.Cmin)
        
        self.stack.append(val)
        

    def pop(self) -> None:
        self.minstack.pop()
        if (len(self.minstack) > 0):
            self.Cmin = self.minstack[-1]
        else:
            self.Cmin = 9999999999999999999999999999999999999999999999999999999999999999999999999999999
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
