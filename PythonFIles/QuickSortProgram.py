
def quicksort(arr, low, high):
    if low<high:
        pivot = partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

def partition(arr, low, high):
    p = arr[low]
    i = low+1
    j = high

    while True:
        while i<=j and arr[i]<p:
            i+=1
        while i<=j and arr[j]>p:
            j-=1
        if i<=j:
            arr[i],arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]

    return j

def userinput():
    print("Enter size of array: ")
    n = int(input())
    arr = []
    print("Enter ELements: ")
    for i in range(n):
        element = int(input())
        arr.append(element)
    print("UnSorted Array: ", arr)
    quicksort(arr,0, n-1)
    print("Sorted Array", arr)

if __name__ == "__main__":  
    userinput()