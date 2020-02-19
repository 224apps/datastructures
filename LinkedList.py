#Node of a single LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    #Add a Node in the list
    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)
    
    #Add a Node at the begining of the list
    def addBeg(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    #Add a Node at the last of the list
    def addLast(self, node):
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next 
        newNode = node
        newNode.next = None
        currNode.next = node
        self.length += 1

    #Add a Node  after a value
    def addAfterValue(self, data,  node):
        newNode = node
        currNode = self.head
        while currNode.next != None or currNode.data != data:
            if currNode.data == data:
                newNode.next = currNode.next
                currNode.next = newNode
                self.length += 1
                return 
            else:
                currNode = currNode.next
        print ("The data provided is not present")
    
    #Add a value at a particular position

    def addAtPos(self, node, pos):
        count = 0
        currNode = self.head
        prevNode = self.head

        if pos > self.length or pos< 0:
            print("The position doesn't exist. Please, enter a valid position")
        else:
            while currNode.next != None  or count < pos:
                count += 1
                if count == pos:
                    prevNode.next = node
                    node.next = currNode
                    self.length += 1
                else:
                    prevNode = currNode
                    currNode = currNode.next 
    #Delete

    def deleteBeg(self):
        if self.length == 0:
            print("There is nothing to delete")
        else:
            self.head = self.head.next 
            self.length -= 1
    # method to delete the last node of the linked list

    def deleteLast(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currNode = self.head
            prevNode = self.head

            while currNode.next != None:
                prevNode = currNode
                currNode = currNode.next
            prevNode.next = None
            self.length -= 1

    #Delete a value
    def deleteValue(self, data):
        if self.length == 0:
            print("The list is empty")
        else:
            prevNode = self.head
            currNode = self.head
            while currNode.next != None or currNode.data != data:
                if currNode.data == data:
                    prevNode.next = currNode.next
                    self.length -= 1
                else:
                    prevNode = currNode
                    currNode = currNode.next
        print "The data provided is not present"
    
    #Delete at a position

    def delete(self, pos):
        count = 0
        prevNode = self.head
        currNode = self.head

        if pos > self.length  or pos< 0:
            print("The position doesn't exist. Please enter a valid position")
        elif pos == 1:
            self.deleteBeg()
        else:
            while currNode.next != None or count < pos:
                count += 1
                if count == pos:
                    prevNode.next = currNode.next
                    self.length -= 1
                    return
                else:
                    prevNode = currNode
                    currNode = currNode.next 

    #Get the length of the list
    def getLength(self):
        return self.length
    
    # return the first Element of the list

    def getFirst(self):
        if self.length == 0:
            print("The list is empty")
        else:
            return self.head.data

    #return the last element of the list

    def  getLastElement(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currNode = self.head
            while currNode.next != None:
                currNode = currNode.next
            return currNode.data

    #return the element at a given position

    def getAtPos(self, pos):
        count = 0
        currNode = self.head
        if pos > self.length  or pos< 0:
            print("The position doesn't exist. Please enter a valid position")
        else:
            while currNode.next != None or count < pos:
                count  = count + 1
                if count == pos:
                    return currNode.data
                else:
                    currNode = currNode.next

    # method to print the whole list
    def print_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next 
             
        print nodeList 

node1 = Node(1)
node2 = Node(3)
node3 = Node(17)
node4 = Node(4)
node5 = Node(19)
ll = LinkedList()
ll.addNode(node1)
ll.addNode(node2)
ll.addNode(node3)
ll.addNode(node4)
ll.addNode(node5)
ll.print_list()


        
    












        
            
        
        



    


            
       


    













    

    
    

