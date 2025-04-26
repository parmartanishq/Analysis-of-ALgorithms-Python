"""
# TO TEST THE CODE  
arr = [5, 2, 8, 1, 9, 3, 4]
sort = mergesort(arr)
print(arr)
print(sort)

"""
def mergesort(arr):
    if  len(arr)<= 1:
        return arr
    mid = len(arr) //2
    
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)
    
    return merge(left_arr,right_arr)

def merge(left,right):
    
    sorted = []
    i,j = 0,0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    
    return sorted    

def userinput():
    print("Enter size of array: ")
    n = int(input())
    arr = []
    print("Enter ELements: ")
    for i in range(n):
        element = int(input())
        arr.append(element)
    print("UnSorted Array: ", arr)
    sort = mergesort(arr)
    print("Sorted Array", sort)
    
if __name__ == "__main__":  
    userinput()