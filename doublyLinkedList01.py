class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def insert(self, data):
        newNode = Node(data)
        
        #checking list is empty or not
        if(self.head == None):
            self.head = self.tail = newNode #both head and tail will point to new Node
            self.head.prev = None #initially tail and head both will points to Null
            self.tail.next = None
        else:
            self.tail.next = newNode #if linked list is not empty, then tail next will point to new Node
            newNode.prev = self.tail #and newNode prevevious will point to last node's tail
            self.tail = newNode #changing the tail pointer to new node
            self.tail.next = None #now new nodes tail pointer is points to Null
            
            
    def display(self):
        curr = self.head
        if self.head == None:
            print("doubly linked list is empty")
            return
        else:
            print("nodes of doubly linked list is: ")
            while curr != None:
                print(curr.data,"->",end=" ") 
                curr = curr.next

dList = doublyLinkedList()
dList.display()
dList.insert(5)
dList.insert(4)
dList.insert(6)
dList.insert(3)
dList.insert(2)
dList.display()