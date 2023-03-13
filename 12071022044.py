class stack:
    def __init__(self,maxsize):
        self.top=-1
        self.ms=maxsize
        self.arr=[None]*maxsize
    def isempty(self):
        return self.top==-1
    def isfull(self):
        return self.top==self.ms-1
    def push(self,ele):
        if self.isfull():
            print("full")
        else:
            self.top+=1
            self.arr[self.top]=ele
    def pop(self):
        if self.isempty():
            return ("stack is empty")
        else:
            ele=self.arr[self.top]
            self.top -=1
            return ele
    def peek(self):
        return (self.arr[self.top])
        
    def __str__(self):
        data=[]
        for i in range(self.top+1):
            data.append(self.arr[i])
        return str(data)
    
Q=" "
s=stack(50)
#P = "(A-(B/(C+D))*E^F/G)*H%I"
P ="(A-(B/(C+D))*E^F/G)*H%I"
operators=['(',')','+','-','*','/','%','^']
preced={'^':3,'*':2,'/':2,'%':2,'+':1,'-':1}
for ch in P:
    if ch.isalpha():
        Q = Q + ch
    
    elif ch in operators:
        if ch=='(':
            s.push(ch)
        elif s.peek()==None or s.peek()=='(':
            s.push(ch)
        elif ch==')':
            while s.peek()!='(':
                Q +=s.pop()
            s.pop()
        elif preced[ch] > preced[s.peek()]:
            s.push(ch)
        elif preced[ch] < preced[s.peek()]:
            while s.peek()!='(' and preced[ch] < preced[s.peek()]:
                Q += s.pop()
            if preced[ch]==preced[s.peek()]:
                Q+=s.pop()
            s.push(ch)
        elif preced[ch]==preced[s.peek()] and ch=='^':
            s.push(ch)
        elif preced[ch]==preced[s.peek()] and ch!='^':
            while s.peek()!='(' and s.peek() != None and preced[ch] == preced[s.peek()]:
                Q += s.pop()
            s.push(ch)
    print("{:<3}  {:<25}  {}".format(ch,str(s),Q))
while s.peek()!=None:
    Q+=s.pop()
print(Q)    