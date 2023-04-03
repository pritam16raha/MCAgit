#reverse linked list containing integer data time: 04:42 to 04:54



class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None
        
    def insertValue(self,data):
        #creating new node.
        node = Node(data, self.head)
        self.head = node
        
    def __str__(self):
        if self.head is None:
            return "Linked list is empty"
        else:
            itr = self.head
            point = ''
            while itr != None:
                point = point + str(itr.data) + '->'
                itr = itr.next
            point = point[:-2]
            return point
        
        
    '''
    ***reverse linked list:
    some step wise process i have to follow.
    *vvi
        step 1: when i reach to 2nd node of original linked list, here currently 2nd is pointing to 3rd node of linked list.
        here my job is, break the link between 2nd and 3rd node. also make another link where, 2nd node will point to previous node of 2nd node.
        ex: linked list is 2 -> 4 -> 6 ->8
        only one iteration : after link linked list will look like: 4 -> 2 
                        here problem will arrise, here linked list cant move forward. as the connection between node 4 and node 6 is gone.
                        so, before breaking the link between 4 -> 6, we will just store the 4.next(currentNode.next) value into another(nextNode) variable,
                        which will track the linked list.
    
    *step 2: make head to tail, means make self.head to point to None
         
    *step 3: make tail to head, means tail node points to None, now change it to point to next node of linked list.
    
    during reversal, if we unlink node from next node, the liked list can be lost. 
    for this reason, 
    '''
    
    def reverseList(self):
        prevNode = None #variable to point to previous node of head node of linked list. this will increment everytime
        currentNode = self.head #currentNode pointing to head of linked list
        
        while currentNode != None: #when current node will reach to None, this loop will terminate
            nextNode = currentNode.next #nextNode is 3rd variable(newNode) to track the linkedList, nextNode holds the address of current.next node 
            currentNode.next = prevNode #in 1st iteration prevNode is pointing to None.
            prevNode = currentNode #now incremention previous 
            currentNode = nextNode
            '''
            currentNode = nextNode
            prevNode = currentNode
            #dont do this, else previous will point to previous.next.next node.
            as currentNode was self.head
            and previous was current - 1 = None
            
            so, make prevNode = currentNode first and then make currentNode = currentNode.next(as i have nextNode, so currentNode = nextNOde)
            '''
        self.head = prevNode 
        '''as prevNode is pointing to current - 1 in this linked list, so when currentNode will reach to None, and loop
        will end, in this situation prevNode will point to last node of the linked list, so just make this last node to self.head of the linked list'''
        
link = linkedList()

link.insertValue(2)
link.insertValue(1)
link.insertValue(4)
link.insertValue(3)
link.insertValue(6)
link.insertValue(5)
link.insertValue(8)
link.insertValue(7)
link.insertValue(10)

print(link)

link.reverseList()

print(link)