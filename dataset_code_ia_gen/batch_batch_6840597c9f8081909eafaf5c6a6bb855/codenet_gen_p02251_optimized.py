n=int(input())
coins=[25,10,5,1]
count=0
for c in coins:
    count+=n//c
    n%=c
print(count)