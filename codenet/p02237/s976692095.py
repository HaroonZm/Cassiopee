N = int(input())
G = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    ls = list(map(int,input().split()))
    u = ls[0] - 1
    for v in ls[2:]:
        G[u][v-1] = 1

for row in G:
    print(' '.join(map(str,row)))