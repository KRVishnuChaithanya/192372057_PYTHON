def div(a,b):
    r=a%b
    q=a//b
    return(r,q)
a=int(input("enter the number"))
b=int(input("enter the number"))
r,q=div(a,b)
print("reminder:",r)
print("quotient:",q)
def min_max(a):
    small=min(a)
    big=max(a)
    return(small,big)
a=[1,2,3,4,6]
small,big=min_max(a)
print("smallest:",small)
print("biggest:",big)
def printall(*args):
    print(args)
printall(2,3,'a')
