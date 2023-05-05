'''
*required functions of tree:
1. create a node
2. insert a node in tree
3. display all nodes of tree
4. search for a node
5. delete a node from the tree
6. find the height of the tree
7. 
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.head = None #initiatially empty tree will point to None.
        
    def createNode(self, data):
        self.head = Node(data)
        return Node(data)
    
    def insertNode(self, data):
        if self.head is None:
            self.createNode(data)
        elif self.head.data > data:
            self.
            