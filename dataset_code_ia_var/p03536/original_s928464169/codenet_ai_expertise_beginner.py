N = int(input())
pairs = []
for i in range(N):
    temp = input().split()
    h = int(temp[0])
    p = int(temp[1])
    pairs.append((h, p))

# Trier la liste par la somme des deux éléments de chaque tuple
pairs.sort(key=lambda x: x[0] + x[1])

INF = 10 ** 18
dp1 = [INF] * (N + 1)
dp2 = [INF] * (N + 1)
dp1[0] = 0

for i in range(1, N + 1):
    for j in range(N + 1):
        dp2[j] = dp1[j]
        if j == 0:
            continue
        if dp1[j - 1] > pairs[i - 1][0]:
            continue
        if dp2[j] > dp1[j - 1] + pairs[i - 1][1]:
            dp2[j] = dp1[j - 1] + pairs[i - 1][1]
    for j in range(N + 1):
        dp1[j] = dp2[j]

for j in range(N, -1, -1):
    if dp1[j] < INF:
        print(j)
        break