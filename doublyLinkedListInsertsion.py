class Node:
    def __init__ (self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        if self.head is None:
            print("Linked List is empty")
            
    def insertData(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
            
            
    def __str__(self):
        if self.head == None:
            return "doubly linked list is empty"
        else:
            itr = self.head
            point = ''
            while itr != None:
                point = point + str(itr.data) + '->'
                itr = itr.next
            point = point[:-2]
            return point
                
if __name__ == '__main__':
    dList = doublyLinkedList()
    print(dList)
    dList.insertData(5)
    dList.insertData(4)
    dList.insertData(6)
    dList.insertData(3)
    dList.insertData(2)
    print(dList)