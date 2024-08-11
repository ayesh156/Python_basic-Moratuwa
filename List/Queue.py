# Queue Implementation in Python

# To implement a queue using the list data structure, there are three requirements.

# A list
# Pointers to the head and tail
# Enqueue and Dequeue functions

def enqueue(queue, value):
    queue.append(value)

def dequeue(queue):
    return queue.pop(0)

my_queue=[]
enqueue(my_queue,'a')
enqueue(my_queue,'b')
enqueue(my_queue,'c')
my_queue
dequeue(my_queue)
dequeue(my_queue)
dequeue(my_queue)
