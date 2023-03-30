class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def insert_at_begining(self,data):
            node = Node(data, self.head)
            self.head = node       

    def tailDelete(self):
        if self.head.next == None:
            self.head = None
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None
            
            
    def display(self):
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


ll2 = LinkedList()
ll2.insert_at_begining(10)
ll2.display()
ll2.tailDelete()
ll2.display()