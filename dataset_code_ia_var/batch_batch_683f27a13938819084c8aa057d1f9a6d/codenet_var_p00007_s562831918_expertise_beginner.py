n = 100
times = int(input())
for i in range(times):
    n = n * 1.05
    if n - int(n) > 0:
        n = int(n) + 1
    else:
        n = int(n)
result = n * 1000
print(result)