class graph:
    
    def __init__(self,adjlist):
        self.adjlist=adjlist
    
    
    def h(self,n):
        # heuristic={
        # 'A':1,
        # 'B':1,
        # 'C':1,
        # 'D':1
        #     }
        
        # return heuristic[n]
        return 1
    def A_star(self,start,end):
        
        q_open=set()
        closed=set()
        
        pred=dict()
        g=dict()
        
        q_open.add(start)
        pred[start]=-1
        g[start]=0
        
        while q_open:
            
            #
            #extract node with least vlue of f
            mini_key=None
            
            for k in q_open:
                if mini_key==None or g[k]+self.h(k)<g[mini_key]+self.h(mini_key):
                    mini_key=k
                    
            #pop q out of q_open
            q=mini_key
            #take q's childrens and put their pred
            # print(q)
            
            if q is end:
                
                temp=end
                path=[]
                path.append(temp)
                while pred[temp] !=-1:
                    path.append(pred[temp])
                    temp=pred[temp]
                
                self.returned_cost=g[end]
                return path[::-1]
            
       
            if q not in self.adjlist:
                q_open.remove(q)
                continue
            
            for child ,val in self.adjlist[q]:
                
                if child not in q_open and child not in closed:  
                    pred[child]=q
                    g[child]=g[q]+ val
                    
                    q_open.add(child)
                    
                else:
                    if g[child]>g[q]+val:
                        g[child]=g[q]+val
                        pred[child]=q
                        
                        if child in closed:
                            closed.remove(child)
                            q_open.add(child)
                    
                
                #end for loop
            q_open.remove(q)
            closed.add(q) 

        
    
if __name__=='__main__':
    

    
    data={ #directed
        'A':[('B',4),('D',6)],
        'B':[('D',3),('C',5),('E',1)],
        'C':[('E',6)],
        'D':[('E',4),('F',1)],
        'E':[('F',2)],
            }
    
    
    # data={#undirected
    #     'A':[('B',1),('C',3),('D',7)],
    #     'B':[('A',1),('D',5)],
    #     'C':[('A',3),('D',12)],
    #     'D':[('A',7),('B',5),('C',12)]
    #         }
    
    start,end='A','F'
    
    g=graph(data)
        
    returned_path=g.A_star(start, end)
    print("Path:",returned_path)
    print("Cost:",g.returned_cost)


