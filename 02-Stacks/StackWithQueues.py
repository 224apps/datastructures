
class Queue(object):
    def __init__(self):
        self.array = []
    def isEmpty(self):
        return len(self.array) == 0
    def size(self):
        return len(self.array)
    def enqueue(self, data):
        self.array.append(data)
    def dequeue(self):
        if self.isEmpty():
            print(" The queue is empty and there is nothing to delete")
            return 
        else:
            data = self.array[0]
            self.array.remove(data)
            return data



class StackWithQueues:
    def __init__(self):
        self.Q1 = Queue()
        self.Q2 = Queue()

    def isEmpty(self):
        return  self.Q1.isEmpty() and self.Q2.isEmpty()

    def push(self, item):

        if self.Q2.isEmpty():
            self.Q1.enqueue(item)
        else:
            self.Q2.enqueue(item)

    def pop(self):
        if self.isEmpty():
            print("There is nothing  to remove in the stack")
        elif self.Q2.isEmpty():
            while  not self.Q1.isEmpty():
                curr = self.Q1.dequeue()
                if self.Q1.isEmpty():
                    return curr
                self.Q2.enqueue(curr)
        else:
            while not self.Q2.isEmpty:
                curr = self.Q2.dequeue()
                if self.Q2.isEmpty():
                    return curr
                self.Q2.enqueue(curr)


def  testStackWithQueues(capacity):
    s = StackWithQueues()
    for i in range(capacity):
        s.push(i)
    for i in range(capacity):
        print(s.pop())





testStackWithQueues(5)

    
