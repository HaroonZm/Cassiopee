N = int(input())
d = list(map(int, input().split()))

res = 0
for i in range(0, N):
    for j in range(i+1, N):
        res = res + d[i] * d[j]

print(res)