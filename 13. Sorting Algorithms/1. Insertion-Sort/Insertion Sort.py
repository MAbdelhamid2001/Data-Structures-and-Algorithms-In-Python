# def Insertion_sort(arr):#qorst complexity O(N^2)
#     #more efficient than bubble sort and selection sort
#     #simple algorithm
#     #space O(1)
#     for i in range(1,len(arr)):
#         for j in range(i,-1,-1):
#             a=arr[i]
#             b=arr[j]
#             if a>b:
#                 continue
#             else:
#                 arr[i],arr[j]=arr[j],arr[i]
#                 i=j
                
    
def Insertion_sort(arr):#worst complexity O(N^2) ,Best(N) #space O(1)
    for i in range(1,len(arr)):
        anchor=arr[i]
        j=i-1
        while j>=0 and anchor<arr[j]:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=anchor

            
    
    
    
    
if __name__=='__main__':
    
    arr=[5,9,2,1,67,34,88,34]
    # arr=[11,9,29,7,2,15,28]
    
    
    Insertion_sort(arr)
    print(arr)

