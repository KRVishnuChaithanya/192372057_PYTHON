n=int(input("enmter a number"))
m=0
sum=0
while(n!=0):
    m=n%10
    sum=sum*10+m
    n=n//10
print(sum)
