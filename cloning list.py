a=[1,2,3,4,5]
b=list(a)
print(b)
print(a is b)
a[0]=100
print(a)
a=[100,2,3,4,5]
print(b)
