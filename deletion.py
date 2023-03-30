'''***deletion 03:53 to 04:05***
1. clear the linked list
2. deletion from head
3. deletion from tail(pop)
4. deletion by value'''

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
    
    #fuction to clear the linked list
    def clearList(self):
        self.head = None #pointing the head to None. as my written logic is, when the head pointer will point to None, means my linked list is empty
    
    #deleting the first node of linked list
    def headRemove(self):
        #if head pointer pointing to none, means list is empty, in that case head.next is not possible.
        if self.head == None:
            print("list is already empty, so removing the head is not possible")
        else:
            self.head = self.head.next #just pointing the "head" to next node
            
    
    #delete from tail
    # def tailRemove(self):
    #     #logic: step 1: i will run a loop till before last node, and step 2: i will break the link between before last node and last node
    #     curr = self.head
    #     #if curr next is already none, it means list has only head item. here we have to delete the head only.
    #     #as delete head function is already exist, so i will call that function.
    #     if curr.next == None:
    #         self.head = None #self.head means now head is pointing to none, means list become empty
    #         return
        
    #     while curr.next.next != None: #step 1
    #         curr = curr.next #in loop only incrementing the curr pointer
    #         #step 2: pointing before last node to None. as tail always points to None
    #     curr.next = None 
    
    def removeTail(self):
        if self.head == None: #ekhane check krchi link list khali kina?
            return None #haan hole, None return korabo.
        if self.head.next == None: #uporer condition false hole ekhane check krbe link list head er porer node khali/None kina
            self.head = None #jodi haan hoy, tahole link list er head k none kore dilei, link list khali hoye jabe
            return None #r none return koriye debo
        curr = self.head #jodi uporer duto condition true na hoy, tokhn curr name akta pointer nebo jeta link list er head k point krbe
        while curr.next.next != None: #r ekhane check krbo, link list er head er porer porer node None kina!
            curr = curr.next #jodi None na hoy tahole curr pointer k curr.next a increment kore debo
        curr.next = None #r loop theke beronor por curr.next k sudhu None kore dilei, last node link list theke kete jabe.
        return self.head #r return kore debo head er value k
        
    
    
    #04:05 to 04:20  deletion of target index
    def targetDel(self, indexElement):
        current = self.head
        
        if self.head == None:
            print("linked list is already empty, so do you want to delete pritam itself")       
            return
        else:
            if current.data == indexElement:
                self.head = self.head.next
                return
                #although i can call the headremove() function here, as i have this funtion
            else:
                while current.next != None:
                    if current.next.data == indexElement:
                        break
                    current = current.next
                #after while there can be two condition.
                #1. item not found
                if current.next == None:
                    print ("index element not found")
                #2. item found.
                else:
                    current.next = current.next.next 
                    #creating the link between node with previous node and after node of the deleted node

    
    
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
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
    # ll.insert_at_begining(7)
    # ll.insertAtTail(0)
    # ll.insertAtTail(1)
    #ll.inserAfterTarget(100,100)
    ll.print()
    #ll.clearList()
    #ll.insert_at_begining(100)  
    # ll.headRemove()
    # ll.headRemove()
    # ll.headRemove()
    # ll.headRemove()
    # ll.headRemove()
    #ll.headRemove()
    #ll.removeTail()
    
    
    ll.targetDel(2)
    
    ll.print()
    
    ll.targetDel(6)
    ll.targetDel(4)
    
    
    ll.print()