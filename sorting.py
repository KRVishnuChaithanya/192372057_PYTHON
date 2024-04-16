a=input("enter the list").split()
a=list(map(eval,a))
for i in range(0,len(a)):
    smallest =min(a[i:])
    sindex=a.index(smallest)
    a[i],a[sindex]=a[sindex],a[i]
print(a)

a=input("enter a list:").split()
a=list(map(int,a))
for i in a:
 j = a.index(i)
 while (j>0):
     if a[j-1] > a[j]:
         a[j-1],a[j] = a[j],a[j-1]
     else:
         break
     j = j-1
 print (a)

 def merge(a,b):
     c = []
     while len(a) != 0 and len(b) != 0:
         if a[0] < b[0]:
             c.append(a[0])
             a.remove(a[0])
         else:
             c.append(b[0])
             b.remove(b[0])
 if len(a) == 0:
     c=c+b
 else:
     c=c+a

def divide(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = divide(x[:middle])
        b = divide(x[middle:])
    return merge(a,b)
x=[38,27,43,3,9,82,10]
c=divide(x)
print(c)
