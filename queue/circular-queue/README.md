# Circular Queue Data Structure

A circular queue is the extended version of a regular queue where the last element is connected to the first element. Thus forming a circle-like structure.

![circular queue represenation](../images/circular-increment.webp)

The main advantage of a circular queue over a simple queue is better memory utilization. If the last position is full and the first position is empty, we can insert an element in the first position. This action is not possible in a simple queue.

## Working of cirular queue

Circular Queue works by the process of circular increment i.e. when we try to increment the pointer and we reach the end of the queue, we start from the beginning of the queue.

Here, the circular increment is performed by modulo division with the queue size. That is,

```if REAR + 1 == size (overflow!), REAR = (REAR + 1)% size = 0 (start of queue)```

### Circular Queue Operations
The circular queue work as follows:

two pointers FRONT and REAR
FRONT track the first element of the queue
REAR track the last elements of the queue
initially, set value of FRONT and REAR to -1
1. Enqueue Operation
check if the queue is full
for the first element, set value of FRONT to 0
circularly increase the REAR index by 1 (i.e. if the rear reaches the end, next it would be at the start of the queue)
add the new element in the position pointed to by REAR
2. Dequeue Operation
check if the queue is empty
return the value pointed by FRONT
circularly increase the FRONT index by 1
for the last element, reset the values of FRONT and REAR to -1

However, the check for full queue has a new additional case:

- Case 1: FRONT = 0 && REAR == SIZE - 1
- Case 2: FRONT = REAR + 1

The second case happens when REAR starts from 0 due to circular increment and when its value is just 1 less than FRONT, the queue is full.

![circular queue operation](../images/circular-queue-program.webp)


