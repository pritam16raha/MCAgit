#03:35 to #insertion from tail 03:32 to 03:53
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    #magic method to find length of linkedlist
    def __len__(self):
        return self.n
    
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node #reassigning new node
         
        #incrementing the counter of node by one with every node creation in linkedList
    
    
    def insertAtTail(self,data):
        newNode = Node(data)
        if self.head == None: #putting a check whene linked list is empty
            self.head = newNode #when list is empty, i am making newly created node to head.
            return #remaing part will not execute
        
        curren = self.head #"curren" is pointer pointing to linked list head
        
        while curren.next != None:
            curren = curren.next
        curren.next = newNode
    
    
    #***insert after target***
    def inserAfterTarget(self, targetNode, data): #target means, where i want to insert my new node
        newNode = Node(data) #step 1: creating a new node
        current = self.head #step 2: initializing current pointer to linked list head
        while current != None: #step 3: starting the loop with current. (if current pointing to "not null", it will return True)
            if current.data == targetNode: #whene element is found, i am breaking the loop
                break
            #incrementing current with every iteration
            current = current.next
        #print(current.data)
        if current != None:
            newNode.next = current.next
            current.next = newNode
        else:
            print ("element not found")   
    #step 4: if the element not found, then current will run till "None"
    ''' if i want to stop before a node: then condition will be (while current.next != None)
        *if i want to stop before two node then condition will be (while current.next.next != None)
        *if i want stop on the node/target node then conditon will be (while current != None)'''    
    
    
    
    def print(self):
        if self.head is None:
            print("Linked list is emty")
            return 
        itr = self.head #itr is like i pointer, pointion to head at starting
        llstr = ''
        while itr != None:
            llstr = llstr+str(itr.data) + '->' #llstr containing previous llstr data + present itr data. 
            itr = itr.next
        llstr = llstr[:-2] #llst wonts show the last two values on screen(slicing operation)
        print(llstr)
    

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(4)
    ll.insert_at_begining(2)
    ll.insert_at_begining(6)
    ll.insert_at_begining(7)
    ll.insertAtTail(0)
    ll.insertAtTail(1)
    ll.inserAfterTarget(100,100)
    #ll.insert_at_begining(100)
    ll.print()