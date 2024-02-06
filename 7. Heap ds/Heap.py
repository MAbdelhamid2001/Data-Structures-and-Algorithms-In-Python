def heapify(arr,size,i):
    
    largest=i
    
    left=2*i+1
    right=2*i+2
    
    if left<size and arr[i]< arr[left]:        
        largest=left
    
    if right<size and arr[largest] <arr[right]:
        largest=right
        
    if largest !=i:
        arr[i],arr[largest] =arr[largest] ,arr[i]
 
        heapify(arr, size, largest)

    
    return arr

def heap_sort(arr):
    
    size = len(arr)
    for i in range((size//2)-1,-1,-1):
        arr = heapify(arr, size, i)
        
    
    l1=[]
    for i in range(size-1,0,-1):
        
        l1.append(arr[0])
        arr[0],arr[i]= arr[i],arr[0]
        arr=heapify(arr, i, 0)
        
    return l1 
        
        
    
def insert(arr,val):
    
    size=len(arr)
    if size==0:
        arr.append(val)
    else:
        arr.append(val)
        size=len(arr)
        for i in range((size//2)-1,-1,-1):
            arr=heapify(arr, size, i)
            
    return arr
    
def delete(arr,val):
    
    for idx,v in enumerate(arr):
        if val==v:
          break  
    
    arr[idx],arr[-1]= arr[-1],arr[idx]
    
    arr.remove(val)
    
    size=len(arr)
    for i in range(((size//2)-1),-1,-1):
        arr=heapify(arr, size, i)
        
    return arr    
    
if __name__=='__main__':
    
    #heap ds is a complete binary tree
    #here we implement max heap
    #max heap is used to implement priority queue
    
    arr1=[3,9,2,1,4,5]
    
    # n=len(arr1)
    # i=(n//2)-1
    # print(i)
    # for i in range(((n//2)-1),-1,-1):
    #     arr1=heapify(arr1, n, i)
    # print(arr1)   
    
    
    # arr1=insert(arr1, 7) 
    # print(arr1)
    
    # arr1=delete(arr1, 4) 
    # print(arr1)
    
    print(heap_sort(arr1))

    