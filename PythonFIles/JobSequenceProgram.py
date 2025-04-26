'''
# TO TEST THE CODE
Jobs = [
    {"profit": 20, "deadline": 2},
    {"profit": 10, "deadline": 1},
    {"profit": 40, "deadline": 1},
    {"profit": 30, "deadline": 2},
    {"profit": 50, "deadline": 3}   ]
    
    result = jobsequence(Jobs)
    print("Jobs Done:", result[0])
    print("Total Profit:", result[1])
'''

def jobsequence(Jobs):
    
    maxi = 0
    n = len(Jobs)
    for i in range(n):
        maxi = max(maxi,Jobs[i]["deadline"])
        
    result = [-1] * maxi
    
    tprofit = 0 
    jobsdone = 0
    
    arr = []
    for i in range(n):
        arr.append([Jobs[i]["profit"], Jobs[i]["deadline"]])
    
    arr.sort(reverse=True)
    
    for i in range(n):
        for j in range(arr[i][1] -1 , -1, -1):
            if result[j] == -1:
                result[j] = i  
                jobsdone+=1
                tprofit += arr[i][0]
                break 
    
    return [jobsdone,tprofit]     

def userinput():  
    Jobs = []
    n = int(input("Enter number of jobs: "))
    for i in range(n):
        profit = int(input(f"Enter profit for job {i+1}: "))
        deadline = int(input(f"Enter deadline for job {i+1}: "))
        Jobs.append({"profit": profit, "deadline": deadline})
    result = jobsequence(Jobs)
    # Output the results
    print("Jobs Done:", result[0])
    print("Total Profit:", result[1])

if __name__ == "__main__":  
    userinput()