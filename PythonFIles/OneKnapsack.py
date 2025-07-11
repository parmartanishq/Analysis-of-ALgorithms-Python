# Define a class for each item
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# 0/1 Knapsack function using Dynamic Programming
def knapsack(items, W):
    n = len(items)
    # Create DP table with (n+1) rows and (W+1) columns
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i-1].weight <= w:
                # Option to include or exclude the item
                include = items[i-1].profit + dp[i-1][w - items[i-1].weight]
                exclude = dp[i-1][w]
                dp[i][w] = max(include, exclude)
            else:
                # Cannot include the item
                dp[i][w] = dp[i-1][w]

    return dp[n][W]  # Maximum profit

# Main block
if __name__ == "__main__":
    # Take input from user
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        profit = int(input(f"Enter profit for item {i+1}: "))
        weight = int(input(f"Enter weight for item {i+1}: "))
        items.append(Item(profit, weight))

    W = int(input("Enter the capacity of the knapsack: "))

    max_profit = knapsack(items, W)
    print(f"\nMaximum profit you can get: {max_profit}")
