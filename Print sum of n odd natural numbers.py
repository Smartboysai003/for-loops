#Print sum of n odd natural numbers
n=int(input())
sum=0
for i in range(n*2):
    if i%2==1:
        sum+=i
print(sum)
