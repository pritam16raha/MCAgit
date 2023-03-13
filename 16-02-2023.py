#campusX 11:41 hours dsa video 0:0 to 1:34 hours.
'''
#in for loop program execution depends on hardware... faster hardware means faaster execution
#time measuring
import time


start = time.time()
for i in range(1,101):
    print(i)

print(time.time()-start) 



#time measuring using while loop, here execution dont depends on hardware
import time


start = time.time()
i=1
while (i<101):
    print(i)
    i+=1

print(time.time()-start)

'''

#problem arrives usnig loops for time measuring
#1. different time for different algorithm- yes
#2. time varies if implimentation changes
#3. different hardware different time
#4. does not work for extremely small input
#5 time varies for different inputs, but cant established a relation


#2 topic:- Counting operations

#3 topic:- Order of growth
#what do we want?
#a. we want to evaluate the algorithm
#b. we want to evaluate scalablity
#c. we want to evaluate in terms of input size(when the input size is infinite times big, then what will be required!)

'''
*goal of order of growth:
1. want to evaluate program's efficiency when input is very big
2. want to express the growth of program's run time as input size grows
3. want to put an upper bound on growth - as tight as possible
4. do not need to pricise
5. we will look at largest factors in run run time (in which section of the program will take the longest to run)
6. thus generally we want tight upper bound on growth, as function of size of input, in worst case


***MEASURING ORDER OF GROWTH: BIG OH NOTATION***

@ big oh notaion measures an upper bound on the asymptotic growth, often called order of growth

@ big on or o() is used to describe wprst case:
    -> worst case occurs often and is the bottleneck when a program runs
    -> express rate of growth of program relative to the input size
    -> evaluate algorithm NOT machine implemantation

example: 
def fact_iter(n):
    answer = 1 #single operation, setting up the value of answer
    while n>1:
        answer *= n #two peration(1. mul the answer with n, 2. save the value in answer)
        n- = 1 #two operation(1.decrementing n, 2.saving the value in n)
    return answer

this program will take 1+5n operation to execute. here n= number of input

*here our goal is to eleminate the addative constant(which is 1 in 1+5n) and eleminate the multiplication constant (which is 5 in 5n)

*lets understant with another example
-> How to count the total number of operation by seeing the equation only

            n^2          +              2n                              +                2
nested loop is present   + number of opeartion inside the loops is 2    + it means 2 operation is present outside the loop
                            and n stand for input size




'''