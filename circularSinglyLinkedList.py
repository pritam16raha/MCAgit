class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    
    def addAtBegin(self, data):
        newNode = Node(data)
        if self.head is None: #as linked list is empty, so head and tail both will point to newNode.
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head 
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.head = newNode
    
    def addAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
            
            
            
    def addAtPosition(self, value, target):
        newNode = Node(value)
        current = self.head
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
        else:
            
            while current.next != self.head:
                #print("loop ekhane esache na")
                if current.next.data == target:
                    #print("loop ekhane")
                    newNode.next = current.next.next
                    current.next = newNode
                    return
                else:
                    current = current.next
    
               
        
    def __str__(self):
        container2 = ''
        if self.head is None: 
            return "linked list is empty"
        else:
            current = self.head
            container2 = container2 + str(current.data) + '<->' #this line is to print the first inserted value, in this case which is '5'. self.head is pointing to 5
            
            while current.next != self.head:
                current = current.next
                container2 = container2 + str(current.data) + '<->'
            container2 = container2[:-3]
            return container2
                   

'''
***WARNING***
if condition is not written carefully, then linked list can enter into infinite loop, as no node is holding None/Null.
'''

    
linked = circularLinkedList()
linked.addAtBegin(10)
linked.addAtBegin(8)
linked.addAtBegin(6)
linked.addAtBegin(4)
linked.addAtBegin(2)
linked.addAtEnd(100)
print(linked)
linked.addAtPosition(50,100)
print(linked)
