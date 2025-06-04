N = int(input())
V = input().split()
for i in range(N):
    V[i] = int(V[i])
V.sort()
m = V[0]
for i in range(1, N):
    m = (m + V[i]) / 2
print(m)