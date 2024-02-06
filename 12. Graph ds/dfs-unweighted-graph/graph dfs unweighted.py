def dfs(data,start,nodes_list=[]):#traversal 
# 


    if start not in nodes_list:
        nodes_list.append(start)
    else:
        return


    for child in data[start]:
        dfs(data,child,nodes_list)
    
    return nodes_list


def dfs_(data,start,visited=set()):#traversal


    if start not in visited:
        print(start,end=" ")
    visited.add(start)

    for child in data[start]-visited:
        dfs_(data,child,visited)
    
    return 



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
    
            
    print(dfs_(data, 'A'))
    print(dfs(data, 'A'))


