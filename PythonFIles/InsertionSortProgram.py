
def insertionSort(arr):
    n = len(arr)

    for i in range (1, n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    print("Sorted Array: ", arr)

def userinput():
    print("Enter size of array: ")
    n = int(input())
    arr = []
    print("Enter ELements: ")
    for i in range(n):
        element = int(input())
        arr.append(element)
    print("UnSorted Array: ", arr)
    insertionSort(arr)

print("PROGRAM TO PERFORM INSERTION SORT")
userinput()

