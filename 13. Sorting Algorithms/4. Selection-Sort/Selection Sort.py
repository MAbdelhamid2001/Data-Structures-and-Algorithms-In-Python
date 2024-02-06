def Selection_sort(arr):# complexity O(N^2)

    for i in range(len(arr)):
        mini_index=i
        for j in range(i,len(arr)):
            if arr[j]<arr[mini_index]:
                mini_index=j
                
        if mini_index !=i:
            arr[i],arr[mini_index]= arr[mini_index],arr[i]
            
    
    
    
    
if __name__=='__main__':
    
    # arr=[5,9,2,1,67,34,88,34]
    arr=[11,9,29,7,2,15,28]
    
    
    Selection_sort(arr)
    print(arr)

