N, K = map(int,input().split())
L = []
for k in range(N):
    L.append(list(map(int,input().split())))
L = sorted(L)
for e in L:
    K -= e[1]
    if K <= 0:
        print(e[0])
        exit(0)