'''
time: 04:30 to 
***question:
1. node
2. insert from head
3. traverse (print)
4. insert from tail
5. insert after target location
6. delete from tail
7. delete from head
8. delete by index value
9. search by target value
'''

#replace maximum value from linked list

class Node:
    def __init__ (self, data = None, next = None):
        self.data = data
        self.next = next
        
class linkedList:
    def __init__ (self):
        self.head = None #becasue initially linked list have no node.
        
    def insertValue(self,data):
        #creating new node.
        node = Node(data, self.head)
        self.head = node
        
    #function to see the linked list
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

    def replaceMax(self, maxValue):
        temp = self.head
        max = temp
        while temp != None:
            if temp.data > max.data:
                max = temp
                #print("loop ekhane akhn")
            else:
                temp = temp.next
                #print("loop aber else e")
        max.data = maxValue
            
               
    
    
    
if __name__=='__main__':
    link2 = linkedList()
    link2.insertValue(18)
    link2.insertValue(5)
    link2.insertValue(6)
    link2.insertValue(9)
    link2.insertValue(12)
    link2.insertValue(15)
    link2.replaceMax(20)

    print(link2)