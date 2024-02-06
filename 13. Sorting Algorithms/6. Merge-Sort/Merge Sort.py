# def Merge_sort(arr):# average O(NlogN) ,complexity worst  O(NlogN)  ,space (n)


#     if len(arr)<2:
#         return arr
    
#     mid=len(arr)//2
    
#     left=arr[:mid]
#     right=arr[mid:]
    
#     left=Merge_sort(left)
#     right=Merge_sort(right)
    
#     return merge(left,right)
    
# def merge(a ,b):
#     sorted_list=[]
#     len_a=len(a)
#     len_b=len(b)
    
#     i=j=0
#     while i<len_a and j<len_b:
#         if a[i]<=b[j]:
#             sorted_list.append(a[i])
#             i+=1
            
#         else:
#             sorted_list.append(b[j])
#             j+=1
            
#     while i<len_a:
#         sorted_list.append(a[i])
#         i+=1

#     while j<len_b:
#         sorted_list.append(b[j])
#         j+=1

#     return sorted_list
    
# if __name__=='__main__':
    
#     # arr=[5,9,2,1,67,34,88,34]
#     arr=[11,9,29,7,2,15,28]
    
    
    
#     print(Merge_sort(arr))

################################################################################
#for more memory optimization we deleted the auxiliary array
def Merge_sort(arr):#space O(1)


    if len(arr)<2:
        return arr
    
    mid=len(arr)//2
    
    left=arr[:mid]
    right=arr[mid:]
    
    Merge_sort(left)
    Merge_sort(right)
    
    return merge_opt(left,right,arr)
    
def merge_opt(a ,b,arr):
    len_a=len(a)
    len_b=len(b)
    
    i=j=k=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
            
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k]=a[i]
        i+=1

    while j<len_b:
        arr[k]=b[j]
        j+=1
        
if __name__=='__main__':
    
    # arr=[5,9,2,1,67,34,88,34]
    arr=[11,9,29,7,2,15,28]
    
    
    Merge_sort(arr)
    print(arr)

