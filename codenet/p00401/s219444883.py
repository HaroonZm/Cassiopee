n = int(input())
count = 0
for i in range(1,n+1):
    if n < 2**(i):
        count = 2**(i-1)
        break
print(count)