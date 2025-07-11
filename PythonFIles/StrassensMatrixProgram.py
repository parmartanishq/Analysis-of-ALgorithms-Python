# Function to add two matrices
def add_matrices(A, B):
    size = len(A)
    return [[A[i][j] + B[i][j] for j in range(size)] for i in range(size)]

# Function to subtract two matrices
def subtract_matrices(A, B):
    size = len(A)
    return [[A[i][j] - B[i][j] for j in range(size)] for i in range(size)]

# Function to pad matrix to next power of 2
def pad_matrix(mat, new_size):
    old_size = len(mat)
    padded = [[0 for _ in range(new_size)] for _ in range(new_size)]
    for i in range(old_size):
        for j in range(old_size):
            padded[i][j] = mat[i][j]
    return padded

# Function to split matrix into quadrants
def split_matrix(mat):
    n = len(mat)
    mid = n // 2
    A11 = [row[:mid] for row in mat[:mid]]
    A12 = [row[mid:] for row in mat[:mid]]
    A21 = [row[:mid] for row in mat[mid:]]
    A22 = [row[mid:] for row in mat[mid:]]
    return A11, A12, A21, A22

# Function to combine 4 quadrants into one matrix
def join_matrices(C11, C12, C21, C22):
    top = [c11 + c12 for c11, c12 in zip(C11, C12)]
    bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
    return top + bottom

# Strassen's recursive matrix multiplication
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    P1 = strassen(add_matrices(A11, A22), add_matrices(B11, B22))
    P2 = strassen(add_matrices(A21, A22), B11)
    P3 = strassen(A11, subtract_matrices(B12, B22))
    P4 = strassen(A22, subtract_matrices(B21, B11))
    P5 = strassen(add_matrices(A11, A12), B22)
    P6 = strassen(subtract_matrices(A21, A11), add_matrices(B11, B12))
    P7 = strassen(subtract_matrices(A12, A22), add_matrices(B21, B22))

    C11 = add_matrices(subtract_matrices(add_matrices(P1, P4), P5), P7)
    C12 = add_matrices(P3, P5)
    C21 = add_matrices(P2, P4)
    C22 = add_matrices(subtract_matrices(add_matrices(P1, P3), P2), P6)

    return join_matrices(C11, C12, C21, C22)

# Function to take matrix input from user
def input_matrix(n, name):
    print(f"\nEnter the elements of Matrix {name} row-wise (space-separated):")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            raise ValueError(f"Each row must have exactly {n} elements.")
        matrix.append(row)
    return matrix

# Main function
def main():
    n = int(input("Enter the size of square matrices (e.g., 2, 3, 4): "))

    A = input_matrix(n, 'A')
    B = input_matrix(n, 'B')

    print("\nMatrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    # Find next power of 2
    next_power = 1
    while next_power < n:
        next_power *= 2

    A_padded = pad_matrix(A, next_power)
    B_padded = pad_matrix(B, next_power)

    result_padded = strassen(A_padded, B_padded)
    result = [row[:n] for row in result_padded[:n]]  # Remove padding

    print("\nResult of Matrix Multiplication using Strassen’s Algorithm:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
