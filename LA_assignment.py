import numpy as np

def input_matrix(rows, cols, name):
    print(f"Enter the elements of matrix {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = input(f"Row {i+1} (space-separated): ").strip().split()
        if len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            return None
        matrix.append([float(x) for x in row])
    return np.array(matrix)

a_rows = int(input("Enter number of rows for matrix A: "))
a_cols = int(input("Enter number of columns for matrix A: "))
b_rows = a_cols  # To ensure AB is defined
b_cols = int(input("Enter number of columns for matrix B: "))

A = input_matrix(a_rows, a_cols, "A")
if A is None:
    exit()
B = input_matrix(b_rows, b_cols, "B")
if B is None:
    exit()

AB = np.dot(A, B)
BA = np.dot(B, A)

print("AB:\n", AB)
print("BA:\n", BA)
print("AB shape:", AB.shape)
print("BA shape:", BA.shape)
print("Are AB and BA equal?", np.array_equal(AB, BA))