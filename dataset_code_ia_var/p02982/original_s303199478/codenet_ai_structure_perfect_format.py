import math

N, D = map(int, input().split())
x = []
count = 0

for i in range(N):
    x.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        s = 0
        for k in range(D):
            s += (x[j][k] - x[i][k]) ** 2
        if math.sqrt(s) == int(math.sqrt(s)):
            count += 1

print(count)