import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    output = sys.stdout.write

    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        G[a].append(b)
        G[b].append(a)

    MOD = 10**9 + 9
    v1, v2 = 13, 17

    # BFS: Obtain vertex order D
    visited = [False] * N
    D = []
    que = deque([0])
    visited[0] = True
    while que:
        v = que.popleft()
        D.append(v)
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                que.append(w)

    # DP phase: Track (height, hash1, hash2) per subtree
    H = [0] * N
    X1 = [0] * N
    X2 = [0] * N
    counter = defaultdict(int)

    for v in reversed(D):
        h = su1 = su2 = 0
        for w in G[v]:
            if H[w]:
                h = max(h, H[w])
                su1 += X1[w]
                su2 += X2[w]
        H[v] = k = h + 1
        X1[v] = w1 = (su1 * v1 + 1) % MOD
        X2[v] = w2 = (su2 * v2 + 1) % MOD
        counter[(k, w1, w2)] += 1

    # Calculate answer using math.comb() if available
    ans = sum(c * (c - 1) // 2 for c in counter.values())
    output(f"{ans}\n")

main()