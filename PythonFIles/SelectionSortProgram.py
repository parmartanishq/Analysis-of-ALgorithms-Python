def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[j]< arr[mini]:
                mini = j
        arr[i],arr[mini] =arr[mini],arr[i]
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
    selectionSort(arr)

if __name__ == "__main__":  
    print("PROGRAM TO PERFORM SELECTION SORT")
    userinput()