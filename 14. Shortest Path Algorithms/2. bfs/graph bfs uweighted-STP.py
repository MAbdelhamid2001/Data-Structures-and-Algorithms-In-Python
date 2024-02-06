from collections import deque

class graph:
    def __init__(self,adjlist):
        self.adjlist=adjlist
    
    #get shortest path for unweighted graph
    #get shortest path for weighted graph

    def bfs_short(self,start,end):
        
        self.dist=dict()
        self.pred=dict()

        visited=set()
        q=deque()
        
        self.dist[start]=0
        self.pred[start]=-1
        
        q.appendleft(start)
        while q:
            
            node=q.pop()
            
            if node not in self.adjlist:
                continue
            
            if node not in visited:
                print(node,end=" ")
            visited.add(node)
            

            for child in self.adjlist[node]:
                if child not in visited:
                    
                    self.dist[child]=self.dist[node]+1
                    self.pred[child]=node
                    
                    q.appendleft(child)
                    
                    if child == end:
                        print(child)
                        return True
                    
        return False

                        
    def shortestpath(self,start,end):
        
        if self.bfs_short(start,end)==False:
            print("no path available")
        
        else:
            path=[]
            temp=end
            path.append(temp)
            
            while self.pred[temp] !=-1:
                path.append(self.pred[temp])
                temp=self.pred[temp]
            
            print("shortest length is:",self.dist[end])
            print("shortest path is:",end=" ")
        
            for i in range(len(path)-1,-1,-1):
                # print(i,end=" ")
                print(path[i],end=" ")
            

if __name__=='__main__':
    
    
    data={
        'A':{'B'},
        'B':{'A','C','D'},
        'C':{'B','E'},
        'D':{'B','E'},
        'E':{'C','D','F'},
        'F':{'E'},
            }
    
    
    
    start,end='A','E'
    g=graph(data)
    g.shortestpath(start, end)
