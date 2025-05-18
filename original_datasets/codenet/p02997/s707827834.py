N, K = map(int,input().split())
if K > (N-1)*(N-2)//2:
    print(-1)
    exit()
M = N-1
cnt = (N-1)*(N-2)//2
edges = []
for i in range(2, N+1):
    edges.append((1, i))
for i in range(2, N+1):
    for j in range(i+1, N+1):
        if cnt == K:
            break
        edges.append((i, j))
        cnt -= 1
        M += 1
    if cnt == K:
        break
print(M)
for u, v in edges:
    print(u, v)