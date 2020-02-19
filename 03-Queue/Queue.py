
class Queue:
    def __init__(self):
        self.array = []

    def isEmpty(self):
        return (len(self.array) == 0)
    
    def size(self):
        return (len(self.array))
    
    def front(self):
        if self.isEmpty():
            return None
        return self.array [0]

    def enqueue(self, data):
        self.array.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("Underflow")
            return  None
        else:
            data = self.array[0]
            self.array.remove(data)
            return data

import random
def testQueue():
    q = Queue()
    c = 5
    while(c):
        data = random.randrange(1,100)
        print ("Enqueuing {}".format(data))
        q.enqueue(data)
        c -= 1
    print("Queue size {} ".format(q.size()))
    c = 5
    while(c):
        print("Dequeueing {}".format(q.dequeue()))
        c -= 1

testQueue()
