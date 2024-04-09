rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
print("Enter the elements row-wise:")
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input())
        row.append(element)
    matrix.append(row)
print("Matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  
