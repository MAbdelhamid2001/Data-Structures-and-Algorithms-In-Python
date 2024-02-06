def linear_search(arr,num):
    for idx,val in enumerate(arr):
        if val==num:
            return idx
    return -1
    
def binary_search(arr,num):
    
    left_idx=0
    right_idx=len(arr)-1
    mid_idx=0
    while left_idx <= right_idx:
        mid_idx =(left_idx+right_idx)//2
        
        if num==arr[mid_idx]:
            return mid_idx
            
        if num<arr[mid_idx]:
            
            right_idx=mid_idx-1
        else:
            left_idx =mid_idx+1
    return -1


# def binary_search_rec(arr,num,left_idx,right_idx):
    
#     if right_idx<left_idx:
#         return -1
 
#     mid_idx =(left_idx+right_idx)//2
    
#     mid_value=arr[mid_idx]
    
#     if num==mid_value:
#         return mid_idx
        
#     if num<mid_value:
        
#         right_idx=mid_idx-1
#         return binary_search_rec(arr,num,left_idx,right_idx)
        
#     else:
#         left_idx =mid_idx+1
#         return binary_search_rec(arr,num,left_idx,right_idx)


def binary_search_rec(arr,num,left_idx,right_idx):
    
    if right_idx<left_idx:
        return -1
 
    mid_idx =(left_idx+right_idx)//2
    
    mid_value=arr[mid_idx]
    
    if num==mid_value:
        return mid_idx
        
    if num<mid_value:
        
        right_idx=mid_idx-1        
    else:
        left_idx =mid_idx+1
    return binary_search_rec(arr,num,left_idx,right_idx)


if __name__=='__main__':
    
    arr=[12,15,17,19,21,24,54,67]
    

    # idx=binary_search(arr, 12) 
    # print(idx)
        
    
    left_idx=0
    right_idx=len(arr)-1
    num=16

    idx=binary_search_rec(arr,num,left_idx,right_idx)

    print(idx)


