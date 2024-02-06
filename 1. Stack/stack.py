s=[]
s.append(1)
s.append(2)
s.append(3)

print(s.pop())

print(s)


"""
Lifo 
if you have a list with size 10 and put another item 
its new length will be 10 + 2*10 =30
as it go to anther memory area to allocate this new area
and delete the old one  

and this is a problem ,it dont only need to allocte new memory ,
but also copy the exsisting items to put them in new alocated area as well
 

list :
    adding/poping items from left costs O(N)
    often it costs O(N) to add items from right ,as it requires
    pyhon to relocate memory and copy current items to the new location
    


List basicly
append from right O(1) ,often O(N)
pop()from right  O(1), often O(N)

append from left  O(N)
pop()from left  O(N)

""" 
"""
so using list in python like a stack is not recommended

so we will use deque  (double-ended queue)
deque is implemented as a doubly linked list

deque used for crrating stack and queue


if deque is full ,it dicards item the other end ,to let you append item from the other

so it can be used for keeping list of last-seen items

"""

from collections import deque
d=deque(maxlen=5)
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
print(d)
d.append(15)
print(d)

print(deque('play'))
"""
The most important difference between deque and list 
is that the former allows you to perform efficient append and pop operations on both ends of the sequence

.
deque is not efficient in index access
"""









