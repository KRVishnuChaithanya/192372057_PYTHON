def multiply_matrices(matrix1, matrix2):
    result = [[0, 0],
              [0, 0]]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

print("Enter elements of the first matrix (2x2):")
matrix1 = [[int(input()) for _ in range(2)] for _ in range(2)]

print("Enter elements of the second matrix (2x2):")
matrix2 = [[int(input()) for _ in range(2)] for _ in range(2)]

print("First Matrix:")
for row in matrix1:
    print(row)

print("\nSecond Matrix:")
for row in matrix2:
    print(row)

result = multiply_matrices(matrix1, matrix2)
print("\nResult of Matrix Multiplication:")
for row in result:
    print(row)
