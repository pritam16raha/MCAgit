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
            #print("popped value is ",temp)
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
    



'''
text editor: 05:30 to 05:38
to perform undo and redo operation.
lets given srting is 'Hello'. now perform undo, so string will look like 'Hell', if i perform redo, the deleted charecter will be back in the string
and the string looks like 'Hello'.
'''

def textEditor (text , pattern): #text = string and pattern = in which order the string will be edited
    u = Stack() #u means undo operation, delete the charecter from u stack and push it to r Stack.
    r = Stack() #r means redo operation, delete the charecter from r stack and push it to u stack.
    
    for i in text:
        u.push(i)
        
    for i in pattern:
        if i == 'u':        #when 'u' arrive in string, charecter will be popped out from text, and push the deleted charecter into r stack. 
            data = u.pop()  #'data' is temp variable, its job is only to take the value from u stack and push it to r stack
            r.push(data)
        elif i == 'r':
            if r.isEmpty():
                print("pop from r stack can not be performed! do pop from u stack first")
            else:
                data = r.pop()
                u.push(data)
        else:
            print("wrong pattern arrived")
            continue
        
    result = ''
    while not u.isEmpty():
        result = u.pop() + result
    
    print('final string looks like-',result)


'''
*celebrity problem: 05:39 to 05:
in a given matrix one element dont know anyone, but everyone knows him/her.
4x4 matrix : a b c d
           a - 0 1 1
           b 0 - 1 1
           c 1 0 - 1
           d 0 0 0 0
here element(row) -> element(column) is invalid, this is why - written.
and here d dont knows anyone. but a,b,c everyone knows d. here d is celebrity
process: 
'''
L = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]

def findTheCelebrity(L):
    s = Stack()
    




stack = Stack()
    # stack.push(5)
    # stack.push(6)
    # stack.push(7)
    # stack.traverse()
    # stack.pop()
    # stack.traverse()
    # stack.peek()

#reverseString("hello")

textEditor('pritam', 'uuuuuuu')

