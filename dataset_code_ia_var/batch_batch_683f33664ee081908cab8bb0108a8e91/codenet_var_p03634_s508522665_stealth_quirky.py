from heapq import heapify, heappop, heappush

n = int(input())
E = [[*()]*0 for _ in range(n)]
_ = [E[a-1].append((b-1, c)) or E[b-1].append((a-1, c)) for a,b,c in (map(int, input().split()) for _ in range(n-1))]

Q,K = map(int, input().split())
K -= 1

inf = (1<<60)
D = [inf]*n; D[K] = 0
v = bytearray(n)
P = [K]
heapify(P)
while len(P):
    idx = heappop(P)
    v[idx] = 1
    for nxt,cst in E[idx]:
        if D[nxt] > D[idx]+cst:
            D[nxt] = D[idx]+cst
            if not v[nxt]:
                heappush(P,nxt)

for _ in range(Q):
    x,y=(int(u)-1 for u in input().split())
    print(D[x]+D[y])