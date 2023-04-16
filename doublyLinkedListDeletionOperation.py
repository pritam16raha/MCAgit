class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertData(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        newNode.prev = current


    def deleteNode(self): #this method actually delete the first node of doubly linked list
        if self.head is None:
            print("deletion can not be done, as the doubly linked list is already empty") 
            #return is not required, as i am using else    
        else:
            
            if self.head.next is None:
                self.head = None
                #return is not required, as i am using else
            else:
                self.head = self.head.next
                self.head.prev = None

    def deleteLastNode(self):
        if self.head is None:
            print("Last node deletion can not be done, as the doubly linked list is already empty")
        else:
            if self.head.next is None:
                self.head = None
                
            else:
                current = self.head
                while current.next != None:
                    current = current.next
                current.prev.next = None
                self.tail = current.prev
            




    
    def __str__(self):
        if self.head is None:
            return "Doubly Linked List Is Empty"
        else:
            current = self.head
            container2 = ' '
            while current != None:
                container2 = container2 + str(current.data) + ' <-> '
                current = current.next
            container2 = container2[:-5]
            return container2
  

if __name__ == '__main__':
    dList = doublyLinkedList()
    dList.insertData(10)
    dList.insertData(8)
    dList.insertData(6)
    dList.insertData(4)
    dList.insertData(2)
    dList.insertData(1)
    dList.insertData(0)
    
    print(dList)
    
    dList.deleteLastNode()
    dList.deleteLastNode()
    #dList.deleteNode()
    #dList.deleteNode()
    
    print(dList)