import array
l=[6,7,8,9,5]
a=array.array("i",[])
a.fromlist(l)
print(a)
a.append(90)
print(a)
a.insert(4,2)
print(a)
a.pop(1)
print(a)
print(a.index(2))
a.reverse()
print(a)
print(a.count(5))






