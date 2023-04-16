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
                print("deleted node is :",current.data)
            
    def deleteByValue(self, target):
        current = self.head
        if self.head is None :
            print("Doubly linked list is empty, deletion error")
            return
        #else part:
        else:
            if self.head.data == target:
                    self.head = self.head.next
                    return
            else:
                while current.next != None:
                    if current.next.data == target:
                        break
                    current = current.next
                if current.next == None:
                    print("target is not present in the doubly linked list")
                else:
                    current.next = current.next.next
                

    
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
    dList.deleteByValue(6)
    dList.deleteByValue(10)
    dList.deleteByValue(10)
    dList.deleteByValue(2)
    print(dList)
    #dList.deleteLastNode()
    #dList.deleteNode()
    #dList.deleteNode()
    
    #print(dList)