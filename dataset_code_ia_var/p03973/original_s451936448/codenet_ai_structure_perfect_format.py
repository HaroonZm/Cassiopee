import sys

sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().rstrip()

def resolve():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    ans = A[0] - 1
    p = 2
    for a in A[1:]:
        if a < p:
            continue
        elif a == p:
            p += 1
        else:
            ans += (a - 1) // p
    print(ans)

resolve()