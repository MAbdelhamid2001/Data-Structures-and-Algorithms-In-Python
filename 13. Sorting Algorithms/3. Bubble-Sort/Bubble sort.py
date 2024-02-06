#Bubble Sort Complexity O(N^2)
def Bubble_sort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-1-i):# i for decreasing the time
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                
        if not swapped:#if the array alrady sorted
            break
            
    return arr


    


if __name__=='__main__':
    
    arr=[5,9,2,1,67,34,88,34]
    arr=[11,9,29,7,2,15,28]
    
    Bubble_sort(arr)
    print(arr)
