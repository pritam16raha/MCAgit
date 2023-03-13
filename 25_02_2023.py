#linked list traverse 03:25 to 03:31
class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None #whenever node is created, in address part new node will hold null.

class LinkedList:
    #constractor
    def __init__(self):
        self.head = None

    def insert_head(self,value): #method to insert new node in the linked list
        new_node = Node(value) #creating new node
        new_node.next = self.head #creating link with new node, using linked list's head
    
    def __str__(self):
        curr = self.head #curr is pointer, pointing to head of linked list
        
        result = ''
        
        while curr != None:
            result = result + str(curr.data) + '->' 
            curr = curr.next
        return result
        
    
L = LinkedList()
L.insert_head(4)
L.insert_head(5)
L.insert_head(6)
L.insert_head(8)
L.insert_head(9)
L.insert_head(10)
print(L)
'''n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
L.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
'''
#print(L)