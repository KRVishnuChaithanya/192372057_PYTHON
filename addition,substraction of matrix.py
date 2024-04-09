x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[3,4,5],[1,5,7],[8,2,6]]
z=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        z[i][j]=x[i][j]-y[i][j]

for i in range(len(x)):
    for j in range(len(y)):
        print(z[i][j],end=" ")
    print()
