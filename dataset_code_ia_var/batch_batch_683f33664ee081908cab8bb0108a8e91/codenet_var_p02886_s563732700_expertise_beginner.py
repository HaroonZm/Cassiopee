N = int(input())
d = input().split()
for i in range(N):
    d[i] = int(d[i])

res = 0
i = 0
while i < N:
    j = i + 1
    while j < N:
        res = res + d[i] * d[j]
        j = j + 1
    i = i + 1

print(res)