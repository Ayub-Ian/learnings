class Stack:
    """
    A list where the top is at the end.
    The append and pop() operations are both O(1).
    """
     
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
    
    def peek(self):
         return self.items[len(self.items)-1]
    
class ReverseStack:
     """
      A list where the top is at the beginning instead of at the end.
      The insert(0) and pop(0) operations will both require O(n) for a stack of size n.
      """
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.insert(0,item)
    
     def pop(self):
         return self.items.pop(0)
     
     def peek(self):
         return self.items[0]
     
     def size(self):
         return len(self.items)

    
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
    
    def size(self):
        return self.top + 1
    
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
