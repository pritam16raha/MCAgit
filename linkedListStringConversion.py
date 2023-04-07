#convert the unordered given string into human readable sentence. time : 04:54 to 05:06
#test case 1.  if single '*' or '/' received, replace with space.
#test case 2: if consicutive two '*' or '/' occur, then convert it two single space and make next charecter into upper case.
#ex: The/*sky*is//blue --> The Sky is Blue

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
                point = point + str(itr.data) #+ '->'
                itr = itr.next
            #point = point[:-2]
            return point
        
    def StringConversion(self):
        temp = self.head
        
        while temp != None:
            if temp.data == '*' or temp.data == '/':
                temp.data = ' '
                if temp.next.data == '*' or temp.next.data == '/':
                    temp.next.next.data = temp.next.next.data.upper()
                    temp.next = temp.next.next            
            #incrementing temp pointer by one
            temp = temp.next
            
link = linkedList()

link.insertValue('.')
link.insertValue('e')
link.insertValue('u')
link.insertValue('l')
link.insertValue('b')
link.insertValue('/')
link.insertValue('*')
link.insertValue('s')
link.insertValue('i')
link.insertValue('/')
link.insertValue('y')
link.insertValue('k')
link.insertValue('s')
link.insertValue('*')
link.insertValue('/')
link.insertValue('e')
link.insertValue('h')
link.insertValue('t')

link.StringConversion()

print(link)