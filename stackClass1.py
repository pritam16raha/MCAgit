'''time: 05:06 to 05:30 
stack problem with Linked List
1. string Reversal
2. text Editor
3. Balanced paranthese
4. celebrity problem
'''
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None #this return will return binary True or False according to the condition
    
    def push(self, value):
        newNode = Node(value)
        
        newNode.next = self.top # making new node next top previous top. for pictorial description see copy
        self.top = newNode # and making top pointer to point to newNode
             
    def traverse (self):
        temp = self.top
        print("current stack values are ")
        while temp != None:
            print (temp.data)
            temp = temp.next
            

    def peek(self): #this function only return the top value of stack
        if self.isEmpty():
            print ("stack is empty")
            return
        else:
            print("top value of the stack is:", self.top.data)
        
        
    def pop(self): #this will pop out leatest inserted item, so this function will not get any other parameter.
        if self.isEmpty():
            print("stack is empty, nothing is available to print")
            return
        else:
            temp = self.top.data
            print("popped value is ",temp)
            self.top = self.top.next #just points the top to top.next value.... simply deleting top
            return temp
    '''
    *reverse string using stack is not efficient way, as you have to allocate two different stack, one for normal string, another one for reverse string.
    normal stack will hold string like - 'H','E','L','L','O'
    and reverse stack hold the string in - 'O','L','L','E','H'
    time complexity is O(n), and space complexity is o(n), linear
    '''
def reverseString(text): #it is a fucntion, defind outside the class
    
    s = Stack() #s is the object of Stack class.
    
    for i in text:
        s.push(i)
    
    empString = ''
    while not s.isEmpty(): #s is object of Stack class, this is why isEmpty() can be accessed using object name, outside the Stack class.
        empString = empString + s.pop()
    
    print(empString)
    
    
    
    

stack = Stack()
    # stack.push(5)
    # stack.push(6)
    # stack.push(7)
    # stack.traverse()
    # stack.pop()
    # stack.traverse()
    # stack.peek()

reverseString("hello")