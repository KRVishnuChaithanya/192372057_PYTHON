def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transpose = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]
    
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose


matrix=[[int(input())for i in range(3)]for j in range (3)]
print("original matrix")

for i in matrix:
    print(i)
transposed_matrix=transpose_matrix(matrix)
print("\nTranspose Matrix:")
for i in transposed_matrix:
    print(i)
