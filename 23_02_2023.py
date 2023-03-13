#linked list 02:50 to 00:00 , is collection of nodes
#time cpmplexeity is o(n) for write operation, so when we have to create a application
#which will perform write maximum of time, then we have make a code on linked list rather than array
#dis_adv: read operation take more time than a array, reading will start from first node every time.
#where linked list can be used: stack, queus, doubly linked list, circular linked list.
'''
note: when we print an object like that, print(a), this will print the address, untill i create a str
magic method of this class.
* name of the node itself contains its address. by fetching the object name/node name we can access the
address of the node separetly.
* length of linked list = number of nodes in the linked list

linkedlist: 
            1. Insert
                     1.1 Insert from Head
                     1.2 Insert from Tail (append in python list)
                     1.3 Insert from Middle (insert in python list)
            2. Traverse
                     2.1 Print
            3. Delete
                     3.1 from Head
                     3.1 from Tail(also know as pop in python)
                     3.2 delete the targeted value
                     3.3 delete the targeted indexed value
            4. Search
                     4.1 searche the targeted value
                     4.2 search the targeted index value





'''



'''class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None #whenever node is created, in address part new node will hold null.



class LinkedList:
    #constractor
    def __init__(self):
        self.head = None
        self.n = 0 #counter to count number of nodes in the linkedlist

    #magic method to find length of linkedlist
    def __len__(self):
        return self.n
    
L = LinkedList()
pritam = len(L)
print(pritam)


#03:12 linked list creation and linked list node count

class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None #whenever node is created, in address part new node will hold null.

class LinkedList:
    #constractor
    def __init__(self):
        self.head = None
        self.n = 0 #counter to count number of nodes in the linkedlist

    #magic method to find length of linkedlist
    def __len__(self):
        return self.n

    def insert_head(self,value):
        new_node = Node(value) #creating new node
        new_node.next = self.head #creating link with new node, using linked list's head
        self.n = self.n+1 #whenever new node is connect, the counter of node will be incremented
    
L = LinkedList()
L.insert_head(4)
L.insert_head(8)
L.insert_head(10)
pritam = len(L)
print(pritam)

'''
#linked list traverse 03:25 to 03:31
class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None #whenever node is created, in address part new node will hold null.

class LinkedList:
    #constractor
    def __init__(self):
        self.head = None
        self.n = 0 #counter to count number of nodes in the linkedlist

    #magic method to find length of linkedlist
    def __len__(self):
        return self.n

    def insert_head(self,value): #method to insert new node in the linked list
        new_node = Node(value) #creating new node
        new_node.next = self.head #creating link with new node, using linked list's head
        self.n = self.n+1 #whenever new node is connect, the counter of node will be incremented
    
    def __str__(self):
        curr = self.head #curr is pointer, pointing to head of linked list
        
        result = ''
        
        while curr !=None:
            result = result + str(curr.data) + '->' #this while loop will print every value of node in the linked list
            curr = curr.next #.next of every node already holding the address of next node
        return result[:-2]
    
    
L = LinkedList()
L.insert_head(4)
L.insert_head(5)
L.insert_head(6)
L.insert_head(8)
L.insert_head(9)
L.insert_head(10)
L.len()
