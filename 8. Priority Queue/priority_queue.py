from queue import PriorityQueue


q=PriorityQueue()
q.put((6,'B'))
q.put((2,'A'))
q.put((5,'z'))
q.put((1,'A'))

while not q.empty():
    print(q.get())


print(10*'*')    
    
import heapq

# based on min heap property
letters=[]

heapq.heappush(letters,(6,'B'))
heapq.heappush(letters,(2,'A'))
heapq.heappush(letters,(5,'z'))
heapq.heappush(letters,(3,'A'))

while letters:
    print(heapq.heappop(letters))

# print(heapq.heappop(letters))

# li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
# heapq.heapify(li1)
# # print(heapq.nlargest(2, li1))
# # print(heapq.nsmallest(2, li1))

# print(li1)
 