n=int(input("enmter a number"))
sum=0
t1=0
t2=1
t=t1+t2
i=1
print(t1,t2)
while(i<=n):
    print(t,end="")
    sum=sum+t
    t1=t2
    t2=t
    t=t1+t2
    i=i+1
print("sum=",sum)
