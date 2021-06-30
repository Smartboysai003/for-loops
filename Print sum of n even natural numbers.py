#Print sum of n even natural numbers
n=int(input())
sum=0
for i in range(n*2+1):
    if i%2==0:
        sum+=i
print(sum)
