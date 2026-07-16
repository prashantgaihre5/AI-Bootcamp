def multiply_matrices(mat1, mat2):
    # Determine dimensions
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])

    if cols1 != rows2:
        return None

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
                
    return result

if __name__ == "__main__":
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

    product = multiply_matrices(matrix_A, matrix_B)
    
    if product:
        print("\nProduct of A and B:")
        for row in product:
            print(row)
    else:
        print("\nCannot multiply matrices: invalid dimensions.")
