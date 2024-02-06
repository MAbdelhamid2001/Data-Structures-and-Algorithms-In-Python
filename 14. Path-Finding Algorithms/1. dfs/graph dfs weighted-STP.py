class graph: #weighted graph
    def __init__(self,adjlist):
        self.adjlist=adjlist

    

    def dfs(self,start,visited=[]):#traversal
        
        
        if start not in visited:
            visited.append(start)
            print(start,end=" ")
        else:
            return
    
        if start not in self.adjlist:
            return 
            
        for child,value in self.adjlist[start]:
            self.dfs(child,visited)
                
        
    def dfs_get_shortest_path(self,start,end,path=[],val=0):#traversal
        
        path = path + [start]

        if start == end:
            return path ,val
        
        if start not in self.adjlist:
            return [] ,0
        
        shortest_path=None
        best_value=None
        current_val=val    
        
        for child,value in self.adjlist[start]:
            val=current_val
            if child not in path:
                # print(child ,end=" ")
                val +=value
                ret_path, ret_value=self.dfs_get_shortest_path(child,end,path,val)
                
                if ret_value:
                    if best_value is None or (ret_value < best_value and len(ret_path)<len(shortest_path)):
                        best_value=ret_value
                        shortest_path=ret_path
                    
        return shortest_path,best_value
        

if __name__=='__main__':
    
    #directed graph
    # data={
    #     'A':[('B',4),('D',6)],
    #     'B':[('D',3),('C',5),('E',1)],
    #     'C':[('E',6)],
    #     'D':[('E',4),('F',1)],
    #     'E':[('F',2)],
    #         }
    
    
    #directed graph
    # data={
    #     'A':[('B',1),('C',3),('D',7)],
    #     'B':[('D',5)],
    #     'C':[('D',12)],
    #         }
    
    #undirected graph
    data={
        'A':[('B',1),('C',3),('D',7)],
        'B':[('A',1),('D',5)],
        'C':[('A',3),('D',12)],
        'D':[('A',7),('B',5),('C',12)]
            }
    


    
    
    
    g=graph(data)
    
    print(g.dfs('A'))

    print(g.dfs_get_shortest_path('A','D'))
    
    
    
                
    
