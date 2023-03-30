#till 04:27 hours

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def search(self, item):
        current = self.head
        pos = 0
        
        while current != None:
            if current.data == item:
                return pos
            current = current.next
            pos = pos + 1
        
        return "not found" 
            
    
    def __getItem__(self,index):
        current = self.head
        pos = 0
        
        while current != None:
            if pos == index:
                return current.data
            current = current.next
            pos = pos + 1
        
        return "index Error"
    
    
            
    def insert_at_begining(self,data):
            node = Node(data,self.head)
            self.head = node #reassigning new node
    
    
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
    ll.insert_at_begining(3)
    ll.insert_at_begining(6)
    ll.insert_at_begining(7)
    ll2 = ll.search(10)
    print(ll2)
    ll3 = ll.__getItem__(10)
    print(ll3)
    ll.print()