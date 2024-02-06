#best sorting Algorithms till now #Insertion sort &Bubble sort over selection sort
#merge sort and heap sort over quick sort
def Quick_sort(arr,start,end):    #Average O(nlog(N)) #worst O(n^2)    

    # print(pivot)
    if start < end:
        pi=partition(arr,start,end)
        
        Quick_sort(arr,start,pi-1)
        Quick_sort(arr,pi+1,end)
    
def partition(arr,start,end):
        

    pivot_index=start
    pivot=arr[pivot_index]

    while start<end:
        while start<len(arr) and arr[start]<=pivot:
            start +=1
        #we got left
            
        while arr[end]>pivot:
            end -=1
        #we got right

        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
        
    arr[end],arr[pivot_index]=arr[pivot_index],arr[end]
    
    return end
    

if __name__=='__main__':
    
    arr=[5,9,2,1,67,34,88,34]
    arr=[11,9,29,7,2,15,28]
    
    Quick_sort(arr,0,len(arr)-1)
    print(arr)
