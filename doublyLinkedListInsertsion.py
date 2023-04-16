'''
* Doubly linked list has five method for insertsion.
 1.Insertion when linked list is empty.
 2. Insert at the begining of the linked list.
 3. Insert at the end of linked list.
 4. Insert after a given node.
 5. Insert before a given node.
'''

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
    
    
    #this is actually method of inserting value at the end of the node        
    def insertData(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next != None:
            current = current.next
        #as this is doubly linked list, so link will be created in both direction after ending the while loop
        current.next = newNode 
        newNode.prev = current 
            
    #insert at begining
    #as this is doubly linked list, so link will be created in both direction 
    # linked list look like this: 5 ⇔ 4 ⇔ 6 ⇔ 3 ⇔ 2 
    def insertAtBegining(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else: 
            newNode.next = self.head #created node now hold the head node reference
            self.head.prev = newNode #previous head's prev will store the address of newNode 
            self.head = newNode #finally head pointer will shift to newNode from previous node.
    
    def reverseDoubly(self):
       prevNode = None
       currentNode = self.head
       
       while currentNode != None:
           nextNode = currentNode.next
           currentNode.next = prevNode
           prevNode = currentNode
           currentNode = nextNode
        
       self.head = prevNode
    
    #insert after a given node.
    def insertAfterValue(self, data, target):
        newNode = Node(data)
        current = self.head
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            while current != None:
                if current.data == target:
                    break
                current = current.next
            if current is None: #in case previous 'if' is True, means loop will break, in that case current will not be 'None'. so ***
                print("target value is not present is this linked list")
            else: # *** this condition will execute
                newNode.next = current.next
                newNode.prev = current
                if current.next is not None:  #this condition is checking, is the current pointing to 'tail-Node' of the linked list or not!
                    current.next.prev = newNode
                current.next = newNode #if current is pointing to last node, then new node will be added at last after current, and newNode.next will get None, as current.next = None.
            
    #add value before a node
    def addBefore(self, data , target):
        newNode = Node(data)
        current = self.head
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            while current != None:
                if current.data == target:
                    break
                current = current.next
            if current is None:
                print("target value is not present is this linked list")
            else:
                newNode.next = current
                newNode.prev = current.prev
                if current.prev is not None:
                    current.prev.next = newNode
                else:
                    self.head = newNode
                current.prev = newNode

        
        
    
    
    
    
    
            
    def __str__(self):
        if self.head == None:
            return "doubly linked list is empty"
        else:
            itr = self.head
            point = ''
            while itr != None:
                point = point + str(itr.data) + ' ⇔  '
                itr = itr.next
            point = point[:-4]
            return point
    
    
    
    
    
                
if __name__ == '__main__':
    dList = doublyLinkedList()
    print(dList)
    dList.insertData(5)
    dList.insertData(4)
    dList.insertData(6)
    dList.insertData(3)
    dList.insertData(2)
    dList.insertData(1)
    dList.insertAtBegining(6)
    dList.insertAtBegining(7)
    print(dList)
    #dList.reverseDoubly()
    dList.insertAfterValue(10,3)
    print(dList)
    
    dList.addBefore(15,5)
    
    print(dList)