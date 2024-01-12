class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    # Adding items into the stack
    def push(self, item):
        self.stack.append(item)
        print("pushed item: " + item)

        # Removing an element from the stack
    def pop(self):
        if (self.is_empty()):
            return "stack is empty"

        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
class FixedStack:
    def __init__(self, MAX_SIZE) -> None:
        self.stack = [None] * MAX_SIZE
        self.top = -1
        self.MAX_SIZE = MAX_SIZE
    
    def is_full(self):
        if(self.top == self.MAX_SIZE):
            return True
        else:
            return False
    
    def is_empty(self):
        if(self.top == -1):
            return True
        else:
            return False
        
    def push(self, data):
        if(self.is_full()):
            print("Could not insert data, Stack is full.")
        else:
            self.top = self.top + 1
            self.stack[self.top] = data
        return data
    
    def pop(self):
        if(self.is_empty()):
            print("Could not retrieve data, Stack is empty.")
        else:
            data = self.stack[self.top]
            self.stack[self.top] = None
            self.top = self.top - 1
            
        return data
    
    def peek(self):
        return self.stack[self.top]
    
    def display(self):
        print(self.stack)


if __name__ == "__main__":

    fixed_stack = FixedStack(8)

    fixed_stack.push(44)
    fixed_stack.push(10)
    fixed_stack.push(62)
    fixed_stack.push(123)
    fixed_stack.push(15)

    fixed_stack.display()

    fixed_stack.pop()

    fixed_stack.display()

    print(fixed_stack.peek())
    print(fixed_stack.is_empty())
    print(fixed_stack.is_full())
