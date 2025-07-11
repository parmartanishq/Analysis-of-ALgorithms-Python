def is_safe(board, row, col, n):
    # Check vertically above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True  # Safe to place queen

# This function tries to place queens row by row
def solve_n_queens(board, row, n):
    # If all queens are placed, print the solution
    if row == n:
        print_solution(board, n)
        return True

    res = False  # To check if at least one solution exists

    for col in range(n):
        # Try placing queen at board[row][col]
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            # Recur to place rest of the queens
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = 0  # Backtrack (remove the queen)

    return res

# Function to print the board
def print_solution(board, n):
    print("\nOne of the possible solutions:")
    for row in board:
        for cell in row:
            print("Q" if cell == 1 else ".", end=" ")
        print()

# Main function to handle input
def main():
    try:
        n = int(input("Enter the number of queens (N): "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        # Create an empty NxN chessboard`
        board = [[0 for _ in range(n)] for _ in range(n)]

        # Try solving the N-Queen problem
        if not solve_n_queens(board, 0, n):
            print("No solution exists for N =", n)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main()


