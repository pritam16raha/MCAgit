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
    def createNode(self, data):
        return Node(data)
    
    def insertNode(self, currentNode , data): #currentNode is initial root node
        if currentNode is None:
            return  self.createNode(data)
        if data < currentNode.data:
            currentNode.left = self.insertNode(currentNode.left , data)
        else:
            currentNode.right = self.insertNode(currentNode.right , data)
        return currentNode
    
    
    def traverseInorder(self, root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)
            
            
    def preOrderTraversal(self,root):
        if root is not None:
            print(root.data)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)        
    
    def postOrderTraversal(self, root):
        if root is not None:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.data)        
    
t = Tree()
root = t.createNode(5)
print("root is : ",root.data)
t.insertNode(root , 2)
t.insertNode(root , 10)
t.insertNode(root , 7)
t.insertNode(root , 15)
t.insertNode(root , 12)
t.insertNode(root , 20)
t.insertNode(root , 30)
t.insertNode(root , 6)
t.insertNode(root , 8)

t.traverseInorder(root)
print("preorder list: ")
t.preOrderTraversal(root)

print("post order: ")
t.postOrderTraversal(root)
