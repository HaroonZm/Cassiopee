N, K = map(int, input().split())
cnt = (N - 1) * (N - 2) // 2
if cnt < K:
    print(-1)
    exit()

edges = [[] for _ in range(N)]
for i in range(1, N):
    edges[0].append(i)

ef, et = 1, 2
for i in range(cnt - K):
    edges[ef].append(et)
    et += 1
    if et == ef:
        et += 1
    if et == N:
        ef += 1
        et = ef + 1

M = sum([len(edge) for edge in edges])
print(M)
for u in range(N):
    for v in edges[u]:
        print(u + 1, v + 1)