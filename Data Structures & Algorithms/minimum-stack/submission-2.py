class MinStack:
    #need another stack to keep track of the min values at the time each element is added to the stack
    #in the min_stack, the last element is always the minimum
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        #append to the stack like normal
        self.stack.append(val)
        #this just checks if the stack is still empty and appends it as the default min if it is empty
        if self.min_stack:
            #this appends whichever is lower to the min_stack, compares the new value and the old min
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)
        
    #this pops from both stacks so the minimum reverts to the min at the time that element in the 
    #stack was added
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        return

    def top(self) -> int:
        topval = self.stack[-1]
        return topval

    def getMin(self) -> int:
        return self.min_stack[-1]
        
