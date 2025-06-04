import math

N = int(input())
r = list(map(int, input().split()))

x = [0] * N
x[0] = r[0]

for i in range(1, N):
    max_pos = x[i-1] + 2 * math.sqrt(r[i] * r[i-1])
    for j in range(i-1):
        d = x[j] + 2 * math.sqrt(r[i] * r[j])
        if d > max_pos:
            max_pos = d
    x[i] = max_pos

result = max(x[i] + r[i] for i in range(N)) + r[0]
print(f"{result:.8f}")