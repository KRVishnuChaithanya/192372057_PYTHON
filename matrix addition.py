a=[[1,1],
   [1,1]]
b=[[2,2],
   [2,2]]
c=[[0,0,],
   [0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]
for i in c:
    print(i)

for i in range(len(a)):
    for j in range(len(b)):
         for k in range(len(b)):
             c[i][j]=a[i][j]+a[i][k]*b[k][j]
for i in c:
    print(i)

a=[[1,3],[1,2]]
c=[[0,0],[0,0]]
for i in range(len(a)):
 for j in range(len(a)):
     c[i][j]=a[j][i]
for i in c:
 print(i)
