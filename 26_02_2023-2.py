class Node:
    def __init__(self,data = None, next = None ):
        self.value = data
        self.address = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBegining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        
        curr = self.head
        result = ''
        
        while curr != None:
            result = result + str(curr.value) + "->"
            curr = curr.address
        result = result[:-2]
        print(result)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBegining(1)
    ll.insertAtBegining(2)
    ll.insertAtBegining(3)
    ll.insertAtBegining(4)
    ll.insertAtBegining(5)
    ll.print()