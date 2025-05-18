n = int(input())
a,b = map(int,input().split())
s = n%12
for i in range(1,s+1):
    if i % 2 == 0:
        b = a+b
    else:
        a = a-b
print(a,b)