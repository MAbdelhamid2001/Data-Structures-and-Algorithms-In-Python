from collections import deque

def bfs(data,start):#traversal
    # complexity :O(V+E)
    #using queue
    visited=set()
    queue=deque()
    queue.appendleft(start)
    
    # while queue:
        
    #     node=queue.pop()
    #     if node not in visited: 
    #         print(node,end=" ")
    #     visited.add(node)
        
        
    #     for i in data[node]-visited:
    #         queue.appendleft(i)
    
    while queue:
        
        node=queue.pop()
        if node not in visited: 
            print(node,end=" ")
        visited.add(node)
 
        for i in data[node]:
            if i not in visited:
                queue.appendleft(i)
        
    
        
def bfs_(data,start):#traversal
    
    dis=dict()
    queue=deque()
    queue.appendleft(start)
    dis[start]=0

    while queue:
        parent=queue.pop()
        print(parent,end=" ")
        for child in data[parent]:
            try:
                if dis[child] != 0:
                    dis[child]=dis[parent] +1
            except:
                dis[child]=0
                queue.appendleft(child)
            
                
        
if __name__=='__main__':
    
    data={
        'A':{'B'},
        'B':{'A','C','D'},
        'C':{'B','E','Z'},
        'D':{'B','E'},
        'E':{'C','D','F'},
        'F':{'E'},
        'Z':{'C'}
            }
    
    
            
    # print(dfs_(data, 'A'))
    print(bfs(data, 'A'))
    print(bfs_(data, 'A'))