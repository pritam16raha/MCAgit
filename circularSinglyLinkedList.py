class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class circularLinkedList:
    def __init__(self):
        self.head = None
        
    def insertData(self,data):
        newNode = Node(data)
        if self.head is None: #when linked list is empty, the newly created node -> newnode.next will point to itself. (line no - 14)
            self.head = newNode
            newNode.next = self.head
            return
        current = self.head
        while current.next is not self.head:
            current = current.next
        current.next = newNode
        newNode.next = self.head
        
    def __str__(self):
        container2 = ''
        if self.head is None: 
            return "linked list is empty"
        else:
            current = self.head
            container2 = container2 + str(current.data) + '->'
            
            while current.next != self.head:
                current = current.next
                container2 = container2 + str(current.data) + '->'
            container2 = container2[:-2]
            return container2


'''
***WARNING***
if condition is not written carefully, then linked list can enter into infinite loop, as no node is holding None/Null.


'''


    
linked = circularLinkedList()
linked.insertData(5)
linked.insertData(6)
linked.insertData(4)
linked.insertData(7)
linked.insertData(3)
linked.insertData(8)
linked.insertData(2)
print(linked)
