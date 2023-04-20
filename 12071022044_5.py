class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class linkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        #creating new node.
        node = Node(data, self.head)
        self.head = node
        
    def __len__(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.next
        return count
        
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
        
    def insertBeforeNode(self, value, target):
        newNode = Node(value)
        current = self.head
        if self.head is None:
            self.head = newNode
        elif self.head.data == target:
            self.append(value)           
        else:
            while current.next != None:
                #print("loop ekhane esache na")
                if current.next.data == target:
                    #print("loop ekhane")
                    newNode.next = current.next
                    current.next = newNode
                    return
                else:
                    current = current.next
                    
    def deleteAtFirst(self):
        if self.head == None:
            print("list is already empty, so removing the head is not possible")
        else:
            self.head = self.head.next
        
        
link = linkedList()
link.append(10)
link.append(8)
link.append(6)
link.append(4)
link.append(2)
link.insertBeforeNode(500,2)

print(link)

link.deleteAtFirst()

print(link)

len1 = len(link)
print(len1)
