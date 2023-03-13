#campusX 11:41 hours dsa video 00:00 to 02:50
#dynamic array (python list will be created using array of c)
#'ctypes' is a foreign function library for Python. It provides C compatible data types
 
import ctypes


class pritam_list:
    def __init__(self):
        self.size = 1 #tells size of the array
        self.n = 0 #tells number of element in the array
        #creates a c cype array with size = self.size
        self.A = self.__make_array(self.size)
    
    def __len__(self):
        return self.n #will return the size of the array
    
    def __str__(self):
        result = '' #is empty in initial stage
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']' #[:-1] wont print the last comma in array. without this result looks like= [pritam,3.44,True,10000,]
    
    
    #features to get indexing
    def __getitem__(self,index):
        #condition when index given out of range
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'Given index not present in this array'
        
    #to access 'del', we have to use magic method 02:40
    #ae function amr dewa index er element k delete krbe
    def __delitem__(self,pos): #'pos' hoche, jeta ami delete korte chai
        #check lagabo, jate given index out of list dileo kaaj kore
        if 0 <= pos < self.n:
            #first e shifting krbo
            for i in range(pos,self.n-1): #loop sob somoi position theke cholbe, tar ager element er index aki thakbe
                self.A[i] = self.A[i+1] #right side er element k ak ghor age copy kore debo
            #ter por list er size k ak komabo, jehutu akta element delete hoye gache    
            self.n = self.n - 1
        else:
            print("given index is wrong")
    
    
    
    def append(self,item):
        if self.n == self.size: #checking the array has any empty space or not
            #resize
            self.__resize(self.size*2) #if array has not empty space then we will call that function to create double sized array
        
        #append
        self.A[self.n] = item #inserting given element "item" in the n'th position of the 'A' array.
        self.n = self.n + 1 #item inserted, this is why incrementing the size of the A array n+1
    
    #fatures to delete elements from the array
    def pop(self):
        if self.n == 0: #if the list already empty
            return 'empty list'
        
        print(self.A[self.n-1]) #printing last element is going to delete
        self.n = self.n - 1
    
    def clear(self): #clear will delete all the elements of this list
        #recreating the initial stage only
        self.n = 0
        self.size = 1
        
    def find(self,item): #to find the index of asked element
        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return 'value error'    
    
    
    '''
    def find(self,item): #to find the index of asked element
        for i in range(self.n):
            if self.A[i] == item:
                print (i)
                return
            else:
                print("not found")
                return
    '''
    
    #inserting value in list in targeted location
    def insert(self,pos,item):
        if self.n == self.size: #checking list is full or not
            self.__resize(self.size*2) #if not emplty, then resize function will create new sized list
            
        #shifting the elements to right, and create a space for new item
        for i in range(self.n, pos, -1): #starting the loop from end. 'pos'- loop will stop @ pos+1. '-1'- it is step. position will decrease -1 in every iteration
            self.A[i] = self.A[i-1] #every previous element of the list will be copied to new index in every iteration
        
        self.A[pos] = item #when the loop ends, inserting item in the given position
        self.n = self.n + 1 #as the new item added in the list, so incrementing size of list by one
    
    #this function will delete the targeted vale from the list
    def remove(self,item):
        #as we have created find function to find index, so we will call it
        pos = self.find(item) #this 'item' is removes()'s item, not the find()'s item
        #if the item found, index must be an integer. if not not then it will return string
        if type(pos) == int:
            #delete function k call krbo
            self.__delitem__(pos)
        else:
            return "element not found"
            
    
    
    def __resize(self,new_capacity):
        #create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the content of array A to array B
        for i in range(self.n):
            B[i] = self.A[i]
        #changing the name of array B
        self.A = B
            
        
    def __make_array(self,capacity):
        #creates a c type array (static, referential) with size capacity
        #referential means any type of data type can be stored
        return (capacity*ctypes.py_object)()
    
    
    def sort(self):
        for i in range(0, self.n):
            for j in range(i+1, self.n):
                if (self.A[i] > self.A[j]):
                    temp = self.A[i]
                    self.A[i] = self.A[j]
                    self.A[j] = temp
                    
            
            
        


ll = pritam_list()
'''ll.append("pritam")
ll.append(3.44)
ll.append(True)
ll.append(10000)
ll.append("Morning")'''
ll.append(5)
ll.append(3)
ll.append(4)
ll.append(2)
ll.append(1)
ll.append(2000)
ll.append(99)
ll.append(150)
ll.append(300)
ll.append(500)
ll.append(1000)
ll.append(100)
print(ll)
ll.sort()
#print(ll[0])
#print(ll[1])
#print(ll[2])
#print(ll[3])
#print(ll[4])
#ll.pop()
#print(ll)
#ll.clear()
#pritam = ll.find(10000)
#print(pritam)
#print(ll.find(1000))
#print(ll)
#ll.__delitem__(2)
print(ll)
#ll.remove(True)
#pritam = ll.remove(0000000)
#print(pritam)
#print(ll)