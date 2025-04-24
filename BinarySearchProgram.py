def binarysearch(arr, target):
    left,right = 0, len(arr)-1
    
    while left<=right:
        mid = (left+right)//2
        
        if arr[mid] == target:
            return target
        elif arr[mid] <=target:
            left = mid+1
        elif arr[mid] >= target:
            right = mid -1
    return -1

arr = [1,3,4,6,9,10]
print("ENTER ELEMENT TO SEARCH BETWEEN 1-10: ")
val = int(input())

output = binarysearch(arr,val)

if output == -1:
    print("SORRY ELEMENT NOT FOUND!")
else:
    print("ELEMENT FOUND!: ", output)


            