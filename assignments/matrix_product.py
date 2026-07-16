matrix_A = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix_B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print("Matrix A:")
for row in matrix_A:
    print(row)

print("\nMatrix B:")
for row in matrix_B:
    print(row)

rows1 = len(matrix_A)
cols1 = len(matrix_A[0])
rows2 = len(matrix_B)
cols2 = len(matrix_B[0])

if cols1 != rows2:
    print("\nCannot multiply matrices: invalid dimensions.")
else:
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
                
    print("\nProduct of A and B:")
    for row in result:
        print(row)
