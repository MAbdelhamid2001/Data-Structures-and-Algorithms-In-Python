from collections import deque

class graph: #weighted graph
    def __init__(self,adjlist):
        self.adjlist=adjlist


    def bfs(self,start):#bfs traversal for weighted data 

        visited=set()
        q=deque()
        q.appendleft(start)
        
        while q:
            
            node=q.pop()

            if node not in visited:
                print(node,end=" ")
            visited.add(node)
            
            if node not in self.adjlist:
                continue
            for i,val in self.adjlist[node]:
                if i not in visited:
                    q.appendleft(i)
        

        
if __name__=='__main__':
    
    #directed graph
    data={
        'A':[('B',4),('D',6)],
        'B':[('D',3),('C',5),('E',1)],
        'C':[('E',6)],
        'D':[('E',4),('F',1)],
        'E':[('F',2)],
            }
    
    
    g=graph(data)            
    print(g.bfs('A'))
