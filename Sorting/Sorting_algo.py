def merge(arr,left,mid,right):
    n1 = mid-left+1
    n2 = right-mid
    
    L = [0]*n1
    R = [0]*n2
    
    for i in range(n1):
        L[i] = arr[left+i]
    for j in range(n2):
        R[j] = arr[mid+1+j]
    i = 0
    j = 0
    k = left
    
    while i< n1 and j <n2:
        if L[i] <= R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i <n1:
        arr[k] = L[i]
        i+=1
        k+=1
    
    while j< n2:
        arr[k] = R[j]
        j+=1
        k+=1
        
def merge_sort(arr,left,right):
    if left < right:
        mid = (left+right)//2
        
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx]= arr[min_idx],arr[i]    
        
def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        
        while j>=0 and key<arr[j]:
            arr[j+1]= arr[j]
            j-=1
        arr[j+1]=key

def print_arry(arr):
    for i in arr:
        print(i,end=" ")
    print()
    
if __name__ == "__main__":
    arr = [12,11,13,5,6,7]
    print("Given array is")
    print(arr)
    
    #merge_sort(arr,0,len(arr)-1)
    #selection_sort(arr)
    insertion_sort(arr)
    print(arr)
    
