n=int(input("enmter a number"))
m=0
sum=0
temp=n
while(n!=0):
    m=n%10
    sum=sum*10+m
    n=n//10
print(sum)
if(sum == temp):
    print("palindrome")
else:
    print("not a palindrome")
