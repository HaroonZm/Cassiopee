import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N = int(input())
    Edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        Edge[a-1].append(b-1)
        Edge[b-1].append(a-1)
    C = [int(c) for c in input().split()]
    C.sort(reverse  = True)
    Color = [None] * N
    Color[0] = C[0]
    q = deque()
    for e in Edge[0]:
        q.append((e, 0))
    ans = 0
    for i in range(1, N):
        nowN, preN = q.popleft()
        ans += C[i]
        Color[nowN] = C[i]
        for e in Edge[nowN]:
            if e != preN: q.append((e, nowN))
    print(ans)
    print(" ".join(map(str, Color)))

    return 0

if __name__ == "__main__":
    solve()