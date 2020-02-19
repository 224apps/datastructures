import random
class Stack:
    def __init__(self, C=5):
        self.C = C 
        self.array = []

    def size(self):
        return len(self.array)
    def isEmpty(self):
        return (len(self.array) == 0)
    def isFull(self):
        return (len(self.array) == self.C)
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.array[self.size() - 1]
    def pop(self):
        if self.isEmpty():
            print( "UnderFlow")
            return None
        else:
            data = self.array.pop()
            return data
    def push(self, data):
        if self.isFull():
            print("Overflow")
            return 
        else:
            self.array.append(data)



def testingStack( capacity):
    stack = Stack(capacity)
    newCapacity =  capacity * 2
    while newCapacity:
        data = random.randrange(1,100)
        print("Pushing: {}".format(data))
        stack.push(data)
        newCapacity -= 1
    print ("Stack size: {}".format(stack.size()))

    newCapacity = capacity * 2
    
    while newCapacity:
        print("Popping: {}".format( stack.pop()))
        newCapacity -= 1 

print(testingStack(6))


        
        

    


