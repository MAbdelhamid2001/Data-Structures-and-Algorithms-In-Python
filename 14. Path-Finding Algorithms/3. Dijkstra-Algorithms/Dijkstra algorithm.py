
class graph:#dijkstra using Adjacency list


    def __init__(self,adjlist):
        self.adjlist=adjlist

    def dijkstra(self,start,end): #dijkstra uses bfs and modifie it to get shortest path from source to any other node 
    
        import heapq

        self.dist=dict() #for storing costs
        pq=[] #like in bfs,for storing vertecies ,this priority queue helps in restoring the least cost 
        heapq.heappush(pq, (0,start))
        self.dist[start]=0 #storing costs of the nodes 
        visited=set()
        is_inf_setted=set() #to ensure that all values has infinty as initial value of their cost except (start)
        self.pred=dict() #storing predecessors of nodes,to ease returning shortest path nodes
        self.pred[start]=-1
        
        
        while pq:
            
            value,node = heapq.heappop(pq)
            
                       
            if node not in self.adjlist:
                continue 
            
            if node not in visited:
                # print(node,end=" ") #run the comment to show visited
                pass
            visited.add(node)
 
            for child,dis_val in self.adjlist[node]:
                
                if child not in visited and child not in is_inf_setted:
                    self.dist[child]=float('inf')
                    is_inf_setted.add(child)
                    
                    
                
                if self.dist[child]>self.dist[node]+dis_val:
                    self.dist[child]=self.dist[node]+dis_val
                    heapq.heappush(pq, (self.dist[child],child) )
                    self.pred[child]=node
        
        
        temp=end
        self.path=[]
        self.path.append(temp)
        while self.pred[temp] !=-1:
            self.path.append(self.pred[temp])
            temp=self.pred[temp]
            
        return self.path 
            
    
if __name__=='__main__':
    
    data={
        'A':[('B',4),('D',6)],
        'B':[('D',3),('C',5),('E',1)],
        'C':[('E',6)],
        'D':[('E',4),('F',1)],
        'E':[('F',2)],
            }
    
    
    # data={
    #     'A':[('B',1),('C',3),('D',7)],
    #     'B':[('A',1),('D',5)],
    #     'C':[('A',3),('D',12)],
    #     'D':[('A',7),('B',5),('C',12)]
    #         }
    
    # data={ #graph should be undirected 
    #     '0':[('1',4),('7',8)],
    #     '1':[('0',4),('2',8),('7',11)],
    #     '2':[('1',8),('3',7),('8',2),('5',4)],
    #     '3':[('2',7),('4',9),('5',14)],
    #     '4':[('5',10),('3',9)],
    #     '5':[('6',2),('2',4),('3',14),('4',10)],
    #     '6':[('7',1),('8',6),('5',2)],
    #     '7':[('8',7),('6',1),('0',8),('1',11)],
    #     '8':[('2',2),('6',6),('7',7)]
    #     }
    

    # start,end='0','8'
    
    start,end='A','F'

    g=graph(data)
    
    path=g.dijkstra(start, end)
    print(end='\n')
    print('Distance:',g.dist[end])
    print("shortest path from {0} to {1} :\n".format(start,end),path[::-1])
    
    
    print('Costs:\n',g.dist)
    # print(g.pred)


