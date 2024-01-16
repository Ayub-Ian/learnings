class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.front, self.rear = -1
        self.queue = [None] * k

    
    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.rear + 1) % self.k == self.front):
            print("The circular queue is full\n")

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = data

        # Delete an element from the circular queue
    def dequeue(self):
        if (self.front == -1):
            print("The circular queue is empty\n")

        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.k
            return temp
        
    def printCQueue(self):
        if(self.front == -1):
            print("No element in the circular queue")

        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
           
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
          