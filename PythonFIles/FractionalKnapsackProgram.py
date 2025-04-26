
def fracknapsack(cap, items, n):
    
    arr = []
    tprofit = 0
    crrcap = 0
    
    for i in range(n):
        pw = items[i][0]/items[i][1]
        arr.append([pw,i])
    
    arr.sort(reverse= True)
    
    for i in range(n):
        
        if crrcap+items[arr[i][1]][1] < cap:
            tprofit+= items[arr[i][1]][0]
            crrcap += items[arr[i][1]][1]
        else:
            tprofit += (cap - crrcap)* arr[i][0]
            break
        
    print('\nYOUR TOTAL PROFIT IS: ', tprofit)

def userinput():
    
    n = int(input("ENTER NUMBER OF ITEMS: "))
    cap = int(input("ENTER CAPACITY OF KNAPSACK: "))
   
    items = []
    
    for i in range(n):
        profit = int(input(f"ENTER THE PROFIT OF ITEM {i+1}: ",))
        weight = int(input(f"ENTER THE WEIGHT OF ITEM {i+1}: "))
        items.append((profit,weight))
    
    fracknapsack(cap,items,n)
        
    
if __name__ == "__main__":  
    userinput()