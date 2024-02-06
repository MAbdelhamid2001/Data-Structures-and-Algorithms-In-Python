def Shell_sort(arr):# An optimization for insertion sort , complexity worst O(N(logN)^2) ,Best O(NlogN)

    size=len(arr)
    gap=3
    

    while gap >0:
        for i in range(gap,size):
            anchor=arr[i]
            j=i
            while j>=gap and arr[j-gap]>anchor:
                arr[i]=arr[j-gap]
                j-=gap
            arr[j]=anchor
        gap -=1

    
    
    
    
    
if __name__=='__main__':
    
    arr=[5,9,2,1,67,34,88,34]
    # arr=[11,9,29,7,2,15,28]
    
    
    Shell_sort(arr)
    print(arr)

