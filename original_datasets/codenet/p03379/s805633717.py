n = int(input())
x = list(map(int,input().split()))
y = sorted(x)
for i in range(0,n):
    if x[i] >= y[n // 2]:
        print(y[n // 2 - 1])
    else:
        print(y[n // 2])