N, K = map(int, input().split())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
L.sort()
i = 0
while i < len(L):
    K -= L[i][1]
    if K <= 0:
        print(L[i][0])
        exit(0)
    i += 1