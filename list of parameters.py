def remove(a):
    a.remove(1)
a=[1,2,3,4,5]
remove(a)
print(a)
def inside(a):
 for i in range(0,len(a),1):
     a[i]=a[i]+10
     print("inside",a)
a=[1,2,3,4,5]
inside(a)
print("outside",a)  
def insert(a):
    a.insert(0,30)
a=[1,2,3,4,5]
insert(a)
print(a)
