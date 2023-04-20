#04:39 to \ 04:42
    
    
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
    
    def sumOfOdd(self):
        temp = self.head
        point = 0 #it will iterate over odd position
        sum = 0 #it will store the result of indexed data
        while temp != None:
            if point % 2 != 0:
                sum = sum + temp.data
            
            point = point + 1
            temp = temp.next
        
        print(sum)       
            
    
    
        
link = linkedList()
link.insertValue(0)
link.insertValue(0)
link.insertValue(0)
link.insertValue(2)
link.insertValue(1)
link.insertValue(4)
link.insertValue(3)
link.insertValue(6)
link.insertValue(5)
link.insertValue(8)
link.insertValue(7)
link.insertValue(10)


link.sumOfOdd()

print(link)