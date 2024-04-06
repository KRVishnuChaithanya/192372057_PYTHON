n=int(input("enmter a number"))
m=0
sum=0
temp=n
while(n!=0):
    m=n%10
    sum+=m*m*m
    n=n//10
if(sum == temp):
    print("armstrong number")
else:
    print("not an armstrong number")
