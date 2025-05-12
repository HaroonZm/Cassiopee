n = int(input())
a = list(map(int, input().split()))

x = max(a)

y = 0
for i in range(n):
    if abs(a[i]*2-x)<abs(y*2-x) and a[i]!=x:
        y = a[i]
print(x,end=' ')
print(y)